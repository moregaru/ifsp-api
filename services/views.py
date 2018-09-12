from django.shortcuts import render
from rest_framework import authentication, permissions, viewsets

from .models import Aluno, Auth
from .serializers import AlunoListSerializer, AuthListSerializer
from .filters import AlunoFilter

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

class AlunoViewSet(DefaultMixin,viewsets.ModelViewSet):
    """ Viewset para a listagem dos alunos """

    queryset = Aluno.objects.order_by('nome')
    serializer_class = AlunoListSerializer

    filter_class = AlunoFilter
    filter_fields  = ('nome', 'prontuario',)
    search_fields = ('nome','prontuario', )
    ordering_fields = ('nome', 'prontuario',)



class AuthViewSet(DefaultMixin,viewsets.ModelViewSet):
    queryset = Auth.objects

    serializer_class = AuthListSerializer
