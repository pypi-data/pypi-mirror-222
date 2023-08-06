"""
Amatak Online Shop
Copyright© Amatak Holdings Pty Ltd licensed under the MIT Agreement.
If you interesting to be part of this project pleaese contact:
Rony MAN <amatak.io@outlook.com>
for business <www.amatak.io>
OpenSource <www.amatak.org>
"""
from django.views.generic import ListView, DetailView, View
from amatak_shop.models.item import  Item


class ItemDetailView(DetailView):
    model = Item
    template_name = "amatak_shop/store/product.html"