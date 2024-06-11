from rest_framework import serializers
from hometype.models import HomeType

class HomeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeType
        fields = '__all__'
