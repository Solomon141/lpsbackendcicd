from rest_framework import serializers
from withdrawcustomer.models import WithdrawCustomer
from withdrawal.api.serializers import WithdrawalSerializer

class WithdrawCustomerSerializer(serializers.ModelSerializer):
    tobewithdrawen = WithdrawalSerializer(many=True, read_only=True, required=False)
    
    class Meta:
        model = WithdrawCustomer
        fields = '__all__'
        depth = 1
