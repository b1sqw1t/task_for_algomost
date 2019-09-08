from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.conf import settings

urlpatterns = [
    url('', include('application.urls', namespace='applications')),
    url(r'^account/', include('account.urls', namespace='account')),
    url('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)