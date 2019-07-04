from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^registerProcess$', views.registerProcess, name = 'registerProcess'),
    url(r'^loginProcess$', views.loginProcess, name = 'loginProcess'),
    url(r'^home$', views.home, name = 'home'),
    url(r'^logout$', views.logout, name = 'logout'),
    url(r'^ImageUpload$', views.ImageUpload, name="ImageUpload")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
