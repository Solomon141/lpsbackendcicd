from rest_framework import serializers
from collateralemployee.models import Collateral_Employee
from subcity.api.serializers import SubcitySerializer
from collateralemployeefiles.api.serializers import CollateralEmployeeFilesSerializer

class CollateralEmployeeSerializerInsert(serializers.ModelSerializer):
    class Meta:
        model = Collateral_Employee
        fields = '__all__'


class CollateralEmployeeSerializer(serializers.ModelSerializer):
    salaryfiles = CollateralEmployeeFilesSerializer(many=True, read_only=True, required=False)
    subcity = SubcitySerializer()
    class Meta:
        model = Collateral_Employee
        fields = '__all__'