from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import basket_adding, checkout

urlpatterns = [
    path('basket-adding/', basket_adding, name='basket_adding'),
    path('checkout/', checkout, name='checkout'),
]

