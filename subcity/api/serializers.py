from rest_framework import serializers
from subcity.models import Subcity

class SubcitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcity
        fields = '__all__'


class SubcitySerializerInsert(serializers.ModelSerializer):
    class Meta:
        model = Subcity
        fields = '__all__'
