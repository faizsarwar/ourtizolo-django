from rest_framework import serializers
from .models import *

class infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = info
        fields=(
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "account_type"
        )



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=(
            "id",
            "name",
            "get_absolute_url",
            "description",
            "get_image",
            "get_thumbnail",
            "category",
            "priceRange"
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = '__all__'

class ProductVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductVariation
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=(
            "id",
            "tittle",
            "get_absolute_url",
            "description",
            "get_image",
            "get_thumbnail",
        )

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model=Faq
        fields = '__all__'