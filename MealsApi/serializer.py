from rest_framework import serializers
from .models import MealsData


class MealsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealsData
        fields = ("name","price","description")