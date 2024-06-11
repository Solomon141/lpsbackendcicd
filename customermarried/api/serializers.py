from rest_framework import serializers
from customermarried.models import CustommerMarried
from checklist.api.serializers import CheckListSerializer

class CustommerMarriedSerializer(serializers.ModelSerializer):
    chkmarried = CheckListSerializer()
    class Meta:
        model = CustommerMarried
        fields = '__all__'
        depth = 1

class CustommerMarriedSerializerInsert(serializers.ModelSerializer):
    class Meta:
        model = CustommerMarried
        fields = '__all__'