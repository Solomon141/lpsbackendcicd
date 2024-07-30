from rest_framework import serializers
from withdrawal.models import Withdrawal
from withdrawaldetail.api.serializers import WithdrawalDetailSerializer

class WithdrawalSerializer(serializers.ModelSerializer):
    withdrawaldetail = WithdrawalDetailSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Withdrawal
        fields = '__all__'


class WithdrawalSerializerInsert(serializers.ModelSerializer):
    class Meta:
        model = Withdrawal
        fields = '__all__'
        