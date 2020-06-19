from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from buckets_manager.serializers import CustormAuthTokenSerializer
import logging
# Create your views here.

logger = logging.getLogger(__name__)


class SsoAuthTokenView(ObtainAuthToken):
    """SSO认证后生成token返回"""
    serializer_class = CustormAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        try:
            # sso auth
            token, created = Token.objects.get_or_create(user=username)
            return Response({
                'token': token.key
            })
        except Exception as ex:
            logger.info('sso auth failed {}'.format(str(ex)))

