from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.MainApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
