from rest_framework import serializers
from checklisttype.models import CheckListType
from checklist.api.serializers import CheckListSerializer

class CheckListTypeSerializer(serializers.ModelSerializer):
    checklists = CheckListSerializer(many=True)
    class Meta:
        model = CheckListType
        fields = '__all__'


class CheckListTypeSerializerInsert(serializers.ModelSerializer):
    class Meta:
        model = CheckListType
        fields = '__all__'
