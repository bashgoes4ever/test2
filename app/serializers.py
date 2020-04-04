from rest_framework import serializers
from .models import *

class AppDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppData
        fields = '__all__'


class AppSerializer(serializers.ModelSerializer):
    data = AppDataSerializer(many=True)
    class Meta:
        model = Application
        fields = '__all__'