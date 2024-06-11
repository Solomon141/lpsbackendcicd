from rest_framework import serializers
from carmanufacturer.models import Car_Manufacture

class CarManufactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_Manufacture
        fields = '__all__'
