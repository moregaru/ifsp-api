from django.db import models
from django.utils.translation import ugettext_lazy as _

class Aluno(models.Model):

    prontuario = models.CharField(primary_key=True,max_length=250)
    nome = models.CharField(max_length=250)

    def __str__(self):
        return self.nome or _('Aluno prontuario %s') % self.prontuario

class Auth(models.Model):
	pass