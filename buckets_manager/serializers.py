# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _


class CustormAuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(label=_("Username"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if not username or not password:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')
        return attrs
