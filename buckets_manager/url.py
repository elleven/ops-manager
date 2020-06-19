#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
urlpatterns = [
    url(r'GetApiToken/', views.SsoAuthTokenView.as_view()),
    url(r'', include(router.urls)),
]