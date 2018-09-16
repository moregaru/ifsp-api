from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Auth

class AuthListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = ()