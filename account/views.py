from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.urls import reverse
from random import randrange

from account.models import Profile
from django.contrib.auth.models import User

from application.models import Product
from .forms import LoginForm, ProfileForm


class UserLogin(TemplateView):
    template_name = 'account/login.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = LoginForm
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if not User.objects.filter(username='User').exists():
                create_user = User()
                create_user.username = 'User'
                create_user.set_password('User')
                create_user.save()
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('account:profile'))
                else:
                    kwargs.update({'login_error': 'Аккаунт не активен'})
            else:
                kwargs.update({'login_error': 'Неверный Логин или Пароль.'})
        return super().get(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class Profile(TemplateView):
    template_name = 'account/profile.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not kwargs.get('profile_form', None):
            context['profile_form'] = ProfileForm
        return context

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            if not bool(Product.objects.all().count()):
                for i in range(1, 4):
                    Product.objects.create(name='Продукт {}'.format(i), price=randrange(1000,10000), code=randrange(1,100))
        else:
            kwargs.update({'profile_form': form})
        return super().get(request, *args, **kwargs)