from django.urls import path
from amatak_shop.views.add_coupon import *


app_name = 'amatak_shop'

urlpatterns = [
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
]