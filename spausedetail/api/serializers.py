from rest_framework import serializers
from spausedetail.models import SpauseDetail

class SpauseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpauseDetail
        fields = '__all__'

class SpauseDetailSerializerInsert(serializers.ModelSerializer):
    class Meta:
        model = SpauseDetail
        fields = '__all__'