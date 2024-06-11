from rest_framework import serializers
from customersingle.models import CustommerSingle
from checklist.api.serializers import CheckListSerializer

class CustommerSingleSerializer(serializers.ModelSerializer):
    checkListId = CheckListSerializer()
    class Meta:
        model = CustommerSingle
        fields = '__all__'
        depth = 1


class CustommerSingleSerializerInsert(serializers.ModelSerializer):
    class Meta:
        model = CustommerSingle
        fields = '__all__'
