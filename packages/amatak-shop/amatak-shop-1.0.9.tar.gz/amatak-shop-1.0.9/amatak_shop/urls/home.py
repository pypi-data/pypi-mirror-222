from django.urls import path
from amatak_shop.views.add_coupon import *
from amatak_shop.views.add_to_cart import *
from amatak_shop.views.checkout import *
from amatak_shop.views.create_ref_code import *
from amatak_shop.views.get_coupon import *
from amatak_shop.views.home import *
from amatak_shop.views.is_valid_form import *
from amatak_shop.views.order_summary import *
from amatak_shop.views.payment import *
from amatak_shop.views.policy import *
from amatak_shop.views.products import *
from amatak_shop.views.remove_from_cart import *
from amatak_shop.views.remove_single_item_from_cart import *
from amatak_shop.views.request_refund import *
from amatak_shop.views.terms import *
from amatak_shop.views.items_detail_views import *
from amatak_shop.views.logout import *
from amatak_shop.views.login import *
from amatak_shop.views.sign_up import *



app_name = 'amatak_shop'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('order-summary', OrderSummaryView.as_view(), name='order-summary'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('policy/', policy, name='policy'),
    path('terms/', terms, name='terms'),
    path('logout/', LogoutView, name='account_logout'),
    path('login/', LoginView, name='account_login'),
    path('signup/', SignUpView, name='account_signup'),


]