from rest_framework import serializers
from disbursement.models import Disbursement
from authentication.api.serializers import UserSerializer

class DisbursementSerializer(serializers.ModelSerializer):
    plannedby = UserSerializer()
    disbursedby = UserSerializer()
    checkissuedby = UserSerializer()
    class Meta:
        model = Disbursement
        fields = '__all__'


class DisbursementSerializerInsert(serializers.ModelSerializer):
    
    class Meta:
        model = Disbursement
        fields = '__all__'