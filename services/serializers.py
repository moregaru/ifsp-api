from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Aluno, Auth

class AlunoListSerializer(serializers.ModelSerializer):
    """ LISTA DE ALUNOS """

    link = serializers.SerializerMethodField()

    class Meta:
        model = Aluno
        fields = ('nome', 'prontuario', 'link')
        extra_kwargs = { 
            'link': {'write_only': True}
        }

    def get_link(self,obj):
        request = self.context['request']   
        return {
            'aluno': reverse('aluno-detail',
                kwargs={'pk':obj.pk},request=request),
            'notas': reverse('aluno-detail',
                kwargs={'pk':obj.pk},request=request) + 'notas/',
            'turmas': reverse('aluno-detail',
                kwargs={'pk':obj.pk},request=request) + 'tumas/',
            }

class AuthListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = ()