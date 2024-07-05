# instituto/urls.py
from django.contrib import admin
from django.urls import path, include
from alumnos.views import redireccionar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alumnos/', include('alumnos.urls')),
    path('', redireccionar)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
