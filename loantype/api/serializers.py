from rest_framework import serializers
from loantype.models import LoanType

class LoanTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanType
        fields = ['id', 'enName', 'amName']
