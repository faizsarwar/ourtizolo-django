from rest_framework import serializers
from .models import *


class GtlFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = GtlForm
        fields = ('__all__')