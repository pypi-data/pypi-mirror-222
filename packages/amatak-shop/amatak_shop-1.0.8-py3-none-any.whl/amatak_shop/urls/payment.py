from django.urls import path
from amatak_shop.views.payment import *
from django.views.generic import ListView, DetailView, View

app_name = 'amatak_shop'

urlpatterns = [
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
]