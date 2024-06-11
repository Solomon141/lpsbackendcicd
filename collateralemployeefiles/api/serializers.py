from rest_framework import serializers
from collateralemployeefiles.models import Collateral_EmployeeFiles

class CollateralEmployeeFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collateral_EmployeeFiles
        fields = '__all__'
