"""
Amatak Online Shop
Copyright© Amatak Holdings Pty Ltd licensed under the MIT Agreement.
If you interesting to be part of this project pleaese contact:
Rony MAN <amatak.io@outlook.com>
for business <www.amatak.io>
OpenSource <www.amatak.org>
"""
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404


def SignUpView(request):
    return render(request, "amatak_shop/account/signup.html",)
