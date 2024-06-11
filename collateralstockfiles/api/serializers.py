from rest_framework import serializers
from collateralstockfiles.models import CollateralStockFiles

class CollateralStockFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollateralStockFiles
        fields = '__all__'
