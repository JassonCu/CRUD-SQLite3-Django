from rest_framework import serializers
from .models import Students
from django.utils.translation import gettext_lazy as _
from .validators.validate_phone import validate_phone
from .validators.validate_age import validate_age
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

    def validate_age(self, value):
        validate_age(value)
        return value

    def validate_phone(self, value):
        validate_phone(value)
        return value