from django.urls import path
from amatak_shop.views.add_to_cart import *


app_name = 'amatak_shop'

urlpatterns = [
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
]