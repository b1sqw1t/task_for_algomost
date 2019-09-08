from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from account.models import Profile
from application.models import Product, Order
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm


@method_decorator(login_required, name='dispatch')
class IndexPage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return HttpResponseRedirect(reverse('applications:cart_detail'))

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('applications:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart_detail.html', {'cart': cart})

def cart_all_remove(request):
    cart = Cart(request)
    cart.all_remove()
    return HttpResponseRedirect(reverse('applications:cart_detail'))

def cart_save(request):
    cart = Cart(request)
    for product in cart:
        Order.objects.create(product=product['product'], user_profile=Profile.objects.last(),quantity=product['quantity'], total_price=product['total_price'] )
    cart.all_remove()
    return HttpResponseRedirect(reverse('applications:index_page'))



