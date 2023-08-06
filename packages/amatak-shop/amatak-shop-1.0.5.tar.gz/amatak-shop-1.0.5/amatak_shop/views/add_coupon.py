"""
Amatak Online Shop
Copyright© Amatak Holdings Pty Ltd licensed under the MIT Agreement.
If you interesting to be part of this project pleaese contact:
Rony MAN <amatak.io@outlook.com>
for business <www.amatak.io>
OpenSource <www.amatak.org>
"""
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView, View
from amatak_shop.forms.coupon import CouponForm
from amatak_shop.models.item import Item
from amatak_shop.models.order_item import OrderItem
from amatak_shop.models.order import Order
from amatak_shop.views.get_coupon import get_coupon
from amatak_shop.models.coupon import Coupon
from django.contrib import messages
from django.shortcuts import redirect


class AddCouponView(View):
    def post(self, *args, **kwargs):
        form = CouponForm(self.request.POST or None)
        if form.is_valid():
            try:
                code = form.cleaned_data.get('code')
                order = Order.objects.get(
                    user=self.request.user, ordered=False)
                order.coupon = get_coupon(self.request, code)
                order.save()
                messages.success(self.request, "Successfully added coupon")
                return redirect("amatak_shop:checkout")
            except ObjectDoesNotExist:
                messages.info(self.request, "You do not have an active order")
                return redirect("amatak_shop:checkout")
