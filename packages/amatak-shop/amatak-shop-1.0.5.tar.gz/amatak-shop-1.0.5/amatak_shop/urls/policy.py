from django.urls import path
from amatak_shop.views.policy import *


app_name = 'amatak_shop'

urlpatterns = [
    path('policy/', policy, name='policy')
]