from django.urls import path
from amatak_shop.views.remove_from_cart import *


app_name = 'amatak_shop'

urlpatterns = [
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
]