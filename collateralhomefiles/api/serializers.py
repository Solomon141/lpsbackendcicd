from rest_framework import serializers
from collateralhomefiles.models import CollateralHomeFiles

class CollateralHomeFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollateralHomeFiles
        fields = '__all__'
