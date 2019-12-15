from rest_framework import serializers
from .models import CarModel


class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'
