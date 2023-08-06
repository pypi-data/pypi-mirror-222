from django.urls import path
from amatak_shop.views.remove_single_item_from_cart import *


app_name = 'amatak_shop'

urlpatterns = [
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
]