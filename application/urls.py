from django.conf.urls import url

from application import views

app_name='applications'

urlpatterns = [
    url(r'^$', views.IndexPage.as_view(), name='index_page'),
    url(r'^cart_detail/$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
    url(r'^all_remove/$', views.cart_all_remove, name='cart_all_remove'),
    url(r'^cart_save/$', views.cart_save, name='cart_save')
]
