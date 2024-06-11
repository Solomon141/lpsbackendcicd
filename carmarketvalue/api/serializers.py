from rest_framework import serializers
from carmarketvalue.models import CarMarketValue

class CarMarketValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMarketValue
        fields = '__all__'
