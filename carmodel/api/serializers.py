from rest_framework import serializers
from carmodel.models import Car_Model

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_Model
        fields = '__all__'
