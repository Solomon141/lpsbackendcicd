from rest_framework import serializers
from withdrawaldetail.models import WithdrawalDetail

class WithdrawalDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WithdrawalDetail
        fields = '__all__'
        depth = 1


class WithdrawalDetailSerializerInsert(serializers.ModelSerializer):
    
    class Meta:
        model = WithdrawalDetail
        fields = '__all__'
