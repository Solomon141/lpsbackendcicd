from rest_framework import serializers
from surety.models import Surety

class SuretySerializer(serializers.ModelSerializer):
    class Meta:
        model = Surety
        fields = '__all__'
