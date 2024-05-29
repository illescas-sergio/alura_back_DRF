from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from products.models import Product



class CustomUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        min_length=8, write_only=True)
    
    published_products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    
    def validate_password(self, value):
        return make_password(value)
    
    def validate_username(self, value):
        value = value.replace(" ", "")  # Ya que estamos borramos los espacios
        try:
            user = get_user_model().objects.get(username=value)
            # Si es el mismo usuario mandando su mismo username le dejamos
            if user == self.instance:
                return value
        except get_user_model().DoesNotExist:
            return value
        raise serializers.ValidationError("Nombre de usuario en uso")
    
    def validate_email(self, value):
        # Hay un usuario con este email ya registrado?
        try:
            user = get_user_model().objects.get(email=value)
        except get_user_model().DoesNotExist:
            return value
        # En cualquier otro caso la validación fallará
        raise serializers.ValidationError("Email en uso")

    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'password', 'published_products']


class UserOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username']



class RegisterUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        min_length=8, write_only=True)
    
    def validate_password(self, value):
        return make_password(value)

    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'password']

