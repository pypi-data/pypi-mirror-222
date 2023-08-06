from django.urls import path
from amatak_shop.views.checkout import *


app_name = 'amatak_shop'

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]