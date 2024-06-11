from rest_framework import serializers
from collateralcar.models import Collateral_Car

from carcommonfiles.api.serializers import CarFilesSerializer
from carmodel.api.serializers import CarModelSerializer
from carmanufacturer.api.serializers import CarManufactureSerializer
from cargaragevalue.api.serializers import GarageReportSerializer
from carmarketvalue.api.serializers import CarMarketValueSerializer 

from subcity.api.serializers import SubcitySerializer


class CollateralCarSerializer(serializers.ModelSerializer):
    carfiles = CarFilesSerializer(many=True, read_only=True, required=False)
    marketvalue = CarMarketValueSerializer(many=True, read_only=True, required=False)
    garageReport = GarageReportSerializer(many=True, read_only=True, required=False)
    model = CarModelSerializer()
    manufacturedYear = CarManufactureSerializer()

    subcity = SubcitySerializer()
    class Meta:
        model = Collateral_Car
        fields = '__all__'
        depth = 2


class CollateralCarSerializerInsert(serializers.ModelSerializer):
    carfiles = CarFilesSerializer(many=True, read_only=True, required=False)
    marketvalue = CarMarketValueSerializer(many=True, read_only=True, required=False)
    garageReport = GarageReportSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Collateral_Car
        fields = '__all__'
