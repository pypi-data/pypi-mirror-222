from django.urls import path
from amatak_shop.views.products import products
from amatak_shop.views.items_detail_views import ItemDetailView

app_name = 'amatak_shop'

urlpatterns = [
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
]