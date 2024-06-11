from rest_framework import serializers
from customer.models import Customer
from loan.api.serializers import LoanSerializer
from customersingle.api.serializers import CustommerSingleSerializer
from customermarried.api.serializers import CustommerMarriedSerializer
from spausedetail.api.serializers import SpauseDetailSerializer
from customercommonfiles.api.serializers import CustomerCommonFilesSerializer

class CustomerSerializer(serializers.ModelSerializer):
    loans = LoanSerializer(many=True, read_only=True, required=False)
    marriedgeneralfiles = CustommerMarriedSerializer(many=True, read_only=True, required=False)
    singlegeneralfiles = CustommerSingleSerializer(many=True, read_only=True, required=False)
    spausedetail = SpauseDetailSerializer(many=True, read_only=True, required=False)
    customercommonfiles = CustomerCommonFilesSerializer(many=True, read_only=True, required=False)
    
    class Meta:
        model = Customer
        fields = '__all__'
        depth = 1
