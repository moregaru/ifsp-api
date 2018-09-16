from django.http import HttpResponse

from django.shortcuts import render
from rest_framework import authentication, permissions, viewsets

from .models import Auth
from .serializers import AuthListSerializer

class DefaultMixin(object):
    """ Configurações de autenticação, filtros e paginação """
    
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )

    permission_classes = (
        permissions.IsAuthenticated,
        permissions.IsAuthenticatedOrReadOnly,
    )

class AuthViewSet(DefaultMixin,viewsets.ModelViewSet):
    queryset = Auth.objects

    serializer_class = AuthListSerializer

    def create(self, request, *args, **kargs):
        pass

    def update(self, request, *args, **kargs):
        pass

    def retrieve(self, request, *args, **kargs):
        pass
