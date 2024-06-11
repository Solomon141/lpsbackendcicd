from rest_framework import serializers
from collateralstock.models import CollateralStock
from collateralstockfiles.api.serializers import CollateralStockFilesSerializer
class CollateralStockSerializer(serializers.ModelSerializer):
    stockfiles = CollateralStockFilesSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = CollateralStock
        fields = '__all__'
        depth = 2

class CollateralStockSerializerInsert(serializers.ModelSerializer):
    class Meta:
        model = CollateralStock
        fields = '__all__'
