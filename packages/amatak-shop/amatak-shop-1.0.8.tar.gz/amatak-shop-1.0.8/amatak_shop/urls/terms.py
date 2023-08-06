"""
Amatak Online Shop
Copyright© Amatak Holdings Pty Ltd licensed under the MIT Agreement.
If you interesting to be part of this project pleaese contact:
Rony MAN <amatak.io@outlook.com>
for business <www.amatak.io>
OpenSource <www.amatak.org>
"""
from django.urls import path
from amatak_shop.views.terms import *


app_name = 'amatak_shop'

urlpatterns = [
    path('terms/', terms, name='terms'),
]