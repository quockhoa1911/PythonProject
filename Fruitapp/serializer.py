from dataclasses import fields
from rest_framework import serializers

from Fruitapp.models import Fruits


class FruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruits
        fields = '__all__'
