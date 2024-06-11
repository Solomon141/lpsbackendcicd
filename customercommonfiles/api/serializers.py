from rest_framework import serializers
from customercommonfiles.models import CustomerCommonFiles

class CustomerCommonFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCommonFiles
        fields = '__all__'
        depth = 1
        
        
class CustomerCommonFilesSerializerInsert(serializers.ModelSerializer):
    class Meta:
        model = CustomerCommonFiles
        fields = '__all__'