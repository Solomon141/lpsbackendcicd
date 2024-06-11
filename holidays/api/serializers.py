from rest_framework import serializers
from holidays.models import Holiday 

class HolidaySerializerInsert(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = '__all__'

class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = '__all__'