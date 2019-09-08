from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout_then_login

app_name = 'account'
urlpatterns = [
    url(r'^login/$', views.UserLogin.as_view(), name='login'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    url(r'^profile/$', views.Profile.as_view(), name='profile'),
]