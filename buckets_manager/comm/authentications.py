#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, BasicAuthentication, TokenAuthentication
import requests

_SSO_URL = getattr('settings', 'SSO_URL', None)


class SsoAuthentication(BaseAuthentication):
    """前端进行sso认证登录，此处只需验证token有效性
    """
    def authenticate(self, request):
        auth_header = request.Meta.get("Authorization")
        if auth_header:
            try:
                headers = {"Authorization": auth_header}
                req = requests.get(url=_SSO_URL, headers=headers)
                pass
            except exceptions.AuthenticationFailed('test'):
                pass

    def authenticate_header(self, request):
        pass


class SsoTokenAuthentication(TokenAuthentication):
    """sso token realm
    """
