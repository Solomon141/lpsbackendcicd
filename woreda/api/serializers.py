from rest_framework import serializers
from woreda.models import Woreda

class WoredaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Woreda
        fields = '__all__'