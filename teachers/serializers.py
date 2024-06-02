from rest_framework import serializers
from .models import Proffesor

class ProffesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proffesor
        fields = '__all__'