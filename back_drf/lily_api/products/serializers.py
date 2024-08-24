from rest_framework import serializers
from .models import *
from lily_api import settings


class BaseProductSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()
    class Meta:
        fields = '__all__'

    def get_img_url(self, obj):
        return f'{settings.BASE_URL}{obj.image.url}'



class ProductBastinaSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        model = ProductBastina


class ProductDASerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        model = ProductDA


class ProductLilySerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        model = ProductLily


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ReviewsBastinaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ReviewsBastina


class ReviewsDASerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ReviewsDA


class ReviewsLilySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ReviewsLily


class StoresLilySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = StoresLily


class StoresDASerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = StoresDA


class StoresBastinaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = StoresBastina