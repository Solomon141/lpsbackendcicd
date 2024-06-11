from rest_framework import serializers
from delegation.models import Delegation

class DelegationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delegation
        fields = '__all__'
        depth = 0

class DelegationSerializerInsert(serializers.ModelSerializer):
    class Meta:
        model = Delegation
        fields = '__all__'
