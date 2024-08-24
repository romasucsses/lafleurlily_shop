from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer

from orders.models import ShippingInfo
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'last_name']


class UserSignUpSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        user = User.objects.create(**validated_data)
        return user


class ShippingAddressSerializer(ModelSerializer):
    class Meta:
        model = ShippingInfo
        fields = '__all__'


