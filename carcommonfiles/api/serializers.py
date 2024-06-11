from rest_framework import serializers
from carcommonfiles.models import Car_Files

class CarFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_Files
        fields = '__all__'
