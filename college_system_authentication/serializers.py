from rest_framework import serializers
from .models import UserAccount

class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    accepted_terms = serializers.BooleanField()

    class Meta:
        model = UserAccount
        fields = ['first_name', 'last_name', 'email', 'phone_number',
                  'password1', 'password2', 'accepted_terms']

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "Las contraseñas no coinciden."})
        if not data['accepted_terms']:
            raise serializers.ValidationError(
                {"accepted_terms": "Debe aceptar los términos y condiciones."})
        return data

    def create(self, validated_data):
        # Remove accepted_terms from validated_data since it isn't part of the UserAccount model's fields
        accepted_terms = validated_data.pop('accepted_terms')
        user = UserAccount.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password1'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number']
        )
        user.accepted_terms = accepted_terms
        user.save()
        return user