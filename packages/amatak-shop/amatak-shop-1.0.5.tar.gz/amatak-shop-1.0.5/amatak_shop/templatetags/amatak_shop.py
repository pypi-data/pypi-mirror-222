import datetime
from django import template
from calendar import month_abbr
from random import randint
from django import template
from django.db.models import Sum
from django.urls import reverse
from django.utils.formats import number_format
from django.utils.timezone import localdate
from amatak_shop.models.order import *

from amatak_shop import __version__
from amatak_shop import __license__
from amatak_shop import __author__
from amatak_shop import __amatak_email__
from amatak_shop import __amatak_site_url__

register = template.Library()



"""
Copyrights
"""

@register.simple_tag(name='current_version')
def current_version():
    return __version__

@register.simple_tag(name='license')
def license():
    return __license__


@register.simple_tag(name='author')
def author():
    return __author__

@register.simple_tag(name='amatak_site_url')
def amatak_site_url():
    return __amatak_site_url__

@register.simple_tag(name='amatak_email')
def amatak_email():
    return __amatak_email__


"""
For Store
"""
@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0

@register.inclusion_tag('amatak_shop/store/tags/sidebar_left.html', takes_context=True)
def store_sidebar_left(context):
    return context

@register.inclusion_tag('amatak_shop/store/tags/store_advertise_red.html', takes_context=True)
def store_advertise_red(context):
    return context

@register.inclusion_tag('amatak_shop/customer/tags/customer_table.html', takes_context=True)
def customer_table(context):
    return context


@register.inclusion_tag('amatak_shop/vendor/tags/vendor_table.html', takes_context=True)
def vendor_table(context):
    return context


"""
For Static
"""
@register.inclusion_tag('amatak_shop/static/tags/styles.html', takes_context=True)
def amatak_static_css(context):
    return context

@register.inclusion_tag('amatak_shop/static/tags/scripts.html', takes_context=True)
def amatak_static_scripts(context):
    return context

@register.inclusion_tag('amatak_shop/static/tags/brand.html', takes_context=True)
def amatak_brand(context):
    return context