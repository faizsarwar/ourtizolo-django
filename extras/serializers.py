from rest_framework import serializers
from .models import *

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

class PressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Press
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

class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Research
        fields=(
            "id",
            "crop",
            "result",
            "ProductUsed",
            "protocol",
            "get_image",
            "get_thumbnail",
        )

class TestemonialSerializer(serializers.ModelSerializer):
    class Meta:
        model=Testemonial
        fields = '__all__'
