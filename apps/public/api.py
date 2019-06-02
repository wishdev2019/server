
from rest_framework import viewsets
from rest_framework.decorators import list_route
from core.decorator.response import Core_connector

from auth.authentication import Authentication


class PublicAPIView(viewsets.ViewSet):

    def get_authenticators(self):
        return [auth() for auth in [Authentication]]

    @list_route(methods=['GET'])
    @Core_connector(pagination=True)
    def get_qrtype(self, request):
        pass




