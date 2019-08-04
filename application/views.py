from django.contrib import messages
from django.core.files.base import ContentFile
from urllib.request import urlopen

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView

from application.forms import UploadImageForm
from application.models import Images


class IndexPage(ListView):
    template_name = 'index.html'
    paginate_by = 20
    model = Images
    context_object_name = 'list'



class UploadImageView(CreateView):
    template_name = 'upload_image.html'
    form_class = UploadImageForm
    success_url = reverse_lazy('index_page')

    def form_valid(self, form):
        if not form.cleaned_data.get('image', None) and form.cleaned_data.get('url', None):
            try:
                instance = form.save(commit=False)
                image_url = self.request.POST.get('url')
                content = urlopen(image_url).read()
                instance.image.save(image_url.split('/')[-1], ContentFile(content), save=False)
                instance.save()
                self.object = form.save()
            except:
                messages.add_message(self.request, messages.ERROR, 'Ошибка бро')
                return redirect(reverse_lazy('upload_image'))
        return super().form_valid(form)


class ViewImage(DetailView):
    pk_url_kwarg = 'id'
    model = Images
    template_name = 'detail_view.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('height', None):
            context['height'] = int(self.request.GET.get('height'))
        else:
            context['height'] = self.object.image.height
        if self.request.GET.get('width', None):
            context['width'] = int(self.request.GET.get('width'))
        else:
            context['width'] = int(self.object.image.width)
        return context