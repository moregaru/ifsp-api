
from rest_framework.routers import DefaultRouter

from .views import AlunoViewSet, AuthViewSet

# Recursos diretos e listagens
router 		= DefaultRouter()
router.register('aluno', AlunoViewSet)
router.register('auth', AuthViewSet)