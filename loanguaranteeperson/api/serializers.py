from rest_framework import serializers
from loanguaranteeperson.models import LoanGuaranteePerson

from collateralcar.api.serializers import CollateralCarSerializer
from collateralhome.api.serializers import CollateralHomeSerializer
from collateralstock.api.serializers import CollateralStockSerializer

class LoanGuaranteePersonSerializer(serializers.ModelSerializer):
    cargp = CollateralCarSerializer(many=True, read_only=True, required=False)
    homegp = CollateralHomeSerializer(many=True, read_only=True, required=False)
    stockgp = CollateralStockSerializer(many=True, read_only=True, required=False)
    
    class Meta:
        model = LoanGuaranteePerson
        fields = '__all__'
        # depth = 1

class LoanGuaranteePersonSerializerSelect(serializers.ModelSerializer):
    class Meta:
        model = LoanGuaranteePerson
        fields = '__all__'
        depth = 0

class LoanGuaranteePersonSerializerInsert(serializers.ModelSerializer):
    class Meta:
        model = LoanGuaranteePerson
        fields = '__all__'