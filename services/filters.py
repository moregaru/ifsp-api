import django_filters
from .models import Aluno

class AlunoFilter(django_filters.FilterSet):
    class Meta:
        model = Aluno
        fields = {
            'nome': ['icontains'],
            'prontuario': ['exact'],
        }
