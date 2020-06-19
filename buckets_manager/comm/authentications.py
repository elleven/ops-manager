#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, BasicAuthentication, TokenAuthentication


class SsoAuthentication(BaseAuthentication):
    """sso custorm realm
       to be continue
    """
    def authenticate(self, request):
        pass

    def authenticate_header(self, request):
        pass


class SsoBasicAuthentication(BasicAuthentication):
    """ override authenticate_credentials()
    """
    def authenticate_credentials(self, userid, password, request=None):
        """改写成通过SSO认证"""
        pass


class SsoTokenAuthentication(TokenAuthentication):
    """sso token realm
       recommend
    """
