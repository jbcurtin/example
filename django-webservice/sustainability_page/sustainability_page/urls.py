import logging
import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

logger = logging.getLogger(__name__)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('webservice.urls')),
]

if settings.DEBUG is True:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
