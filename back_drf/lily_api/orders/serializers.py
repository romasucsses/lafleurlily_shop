from rest_framework.serializers import ModelSerializer
from .models import OrderInfoLily, OrderInfoBastina, OrderInfoDA


class OrderInfoBastinaSerializer(ModelSerializer):
    class Meta:
        model = OrderInfoBastina
        fields = '__all__'


class OrderInfoDASerializer(ModelSerializer):
    class Meta:
        model = OrderInfoDA
        fields = '__all__'


class OrderInfoLilySerializer(ModelSerializer):
    class Meta:
        model = OrderInfoLily
        fields = '__all__'
