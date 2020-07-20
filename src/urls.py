
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import include, path


urlpatterns = [
                  path(r'', include('album.urls')),
                  path(r'', include('register.urls')),
            ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
