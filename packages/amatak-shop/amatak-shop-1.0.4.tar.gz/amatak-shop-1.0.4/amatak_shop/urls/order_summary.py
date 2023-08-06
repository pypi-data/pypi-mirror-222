from django.urls import path
from amatak_shop.views.order_summary import *


app_name = 'amatak_shop'

urlpatterns = [
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
]