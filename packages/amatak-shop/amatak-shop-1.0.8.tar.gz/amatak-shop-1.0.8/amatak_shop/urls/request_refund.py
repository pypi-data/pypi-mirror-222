"""
Amatak Online Shop
Copyright© Amatak Holdings Pty Ltd licensed under the MIT Agreement.
If you interesting to be part of this project pleaese contact:
Rony MAN <amatak.io@outlook.com>
for business <www.amatak.io>
OpenSource <www.amatak.org>
"""
from django.urls import path
from amatak_shop.views.request_refund import *


app_name = 'amatak_shop'

urlpatterns = [
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
]