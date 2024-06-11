from rest_framework import serializers
from cargaragevalue.models import GarageReport

class GarageReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = GarageReport
        fields = '__all__'
