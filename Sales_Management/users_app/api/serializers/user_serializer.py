from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterUserSerializer(serializers.ModelSerializer):
    password_2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_2')
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def validate(self, data):
        passwords = data.get('password')
        password_2 = data.get('password_2')
        
        # Verificar si las contraseñas coinciden
        if passwords != password_2:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})

        email = data.get('email')
        
        # Verificar si el email está vacío
        if not email:
            raise serializers.ValidationError({'email': 'Email field cannot be empty.'})

        # Verificar si el email ya existe
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Email already exists.'})

        return data

    def create(self, validated_data):
        validated_data.pop('password_2')
        user = User.objects.create_user(**validated_data)
        return user
