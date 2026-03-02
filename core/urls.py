from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.edge_admin_site.urls if hasattr(admin.site, 'edge_admin_site') else admin.site.urls),
    path('', admin.site.urls), # Por enquanto, a raiz abre direto no Admin
]

# Garante que as imagens do Cloudinary/Locais carreguem no navegador
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)