from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import home, landing, product

urlpatterns = [
    path('landing/', landing, name='land'),
    path('', home, name='home'),
    path('product/<int:product_id>/', product, name='product'),

  ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
