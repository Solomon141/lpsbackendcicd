from rest_framework import serializers
from jobposition.models import JonbPosition

class JonbPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JonbPosition
        fields = '__all__'