from rest_framework import serializers
from .models import Car


class CarDetailSerializer(serializers.ModelSerializer):
    # Autoadding user who logged in to manage data
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = '__all__'


class CarsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'