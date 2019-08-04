from django.conf.urls import url
from django.urls import path

from application.views import IndexPage, UploadImageView, ViewImage

urlpatterns = [
    url(r'^$', IndexPage.as_view(), name='index_page'),
    url(r'^upload/$', UploadImageView.as_view(), name='upload_image'),
    url(r'^view_image/(?P<id>\d+)/$', ViewImage.as_view(), name='view_images')
]
