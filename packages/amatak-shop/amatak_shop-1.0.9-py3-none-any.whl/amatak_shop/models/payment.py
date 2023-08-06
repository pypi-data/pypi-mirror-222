"""
AutoStore( Automotive Online Shop).
We launch this business Store live at www.autocare7.com
Copyright© Amatak Holdings Pty Ltd licensed under the MIT Agreement.
If you interesting to be part of this project pleaese contact:
Rony MAN <amatak.io@outlook.com>
for business <www.amatak.io>
OpenSource <www.amatak.org>
"""
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django_countries.fields import CountryField
from django.utils import timezone
from django.views.generic import ListView, DetailView, View

from amatak_shop.forms.checkout import CheckoutForm
from amatak_shop.forms.coupon import CouponForm
from amatak_shop.forms.refund import RefundForm
from amatak_shop.forms.payment import PaymentForm
from amatak_shop.models.item import Item
from amatak_shop.models.order_item import OrderItem
from amatak_shop.models.order import Order
from amatak_shop.models.address import Address



class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username