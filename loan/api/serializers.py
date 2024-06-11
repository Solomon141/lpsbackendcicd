from rest_framework import serializers
from decimal import Decimal
import locale

from loan.models import Loan
from loancomment.api.serializers import LoanCommentSerializer
from loanguaranteeperson.api.serializers import LoanGuaranteePersonSerializer, LoanGuaranteePersonSerializerSelect
from collateralemployee.api.serializers import CollateralEmployeeSerializer
from surety.api.serializers import SuretySerializer
from loanwitness.api.serializers import LoanWitnessSerializer
from delegation.api.serializers import DelegationSerializer

from collateralcar.api.serializers import CollateralCarSerializer
from collateralhome.api.serializers import CollateralHomeSerializer
from collateralstock.api.serializers import CollateralStockSerializer
from loanadditionaldocs.api.serializers import LoanAdditionalFilesSerializer

class RoundedField(serializers.Field):
    def to_representation(self, value):
        return round(value, 2)
    
class CommaSeparatedNumberField(serializers.Field):
    def to_representation(self, value):
        try:
            locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # Set the locale for number formatting
        except locale.Error:
            locale.setlocale(locale.LC_ALL, '')  # Use the default locale if the specified one is not available

        return locale.format_string("%d", value, grouping=True)

    def to_internal_value(self, data):
        return int(data.replace(',', ''))  # Remove commas for internal value representation

class LoanSerializer(serializers.ModelSerializer):
    loancomment = LoanCommentSerializer(many=True, read_only=True, required=False)
    collateralcar = CollateralCarSerializer(many=True, read_only=True, required=False)
    collateralhome = CollateralHomeSerializer(many=True, read_only=True, required=False)
    collateralemployee = CollateralEmployeeSerializer(many=True, read_only=True, required=False)
    gp = LoanGuaranteePersonSerializer(many=True, read_only=True, required=False)
    loansurety = SuretySerializer(many=True, read_only=True, required=False)
    loanwitness = LoanWitnessSerializer(many=True, read_only=True, required=False)
    delegatedperson = DelegationSerializer(many=True, read_only=True, required=False)
    collateralstock = CollateralStockSerializer(many=True, read_only=True, required=False)
    loanadditionalfiles = LoanAdditionalFilesSerializer(many=True, read_only=True, required=False)
    
    r_approvedPrincipal = RoundedField(source='approvedPrincipal')
    r_totalSaving = RoundedField(source='totalSaving')
    r_totalShares = RoundedField(source='totalShares')
    r_totalDueForPeriod = RoundedField(source='totalDueForPeriod')
    
    # comma separated and rounded number value 
    rcs_totalDueForPeriod = CommaSeparatedNumberField(source='approvedPrincipal')

    class Meta:
        model = Loan
        fields = '__all__'
        depth = 2

class LoanSerializerInsert(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'


