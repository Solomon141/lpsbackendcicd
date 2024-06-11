from rest_framework import serializers
from collateralhome.models import CollateralHome
from hometype.api.serializers import HomeTypeSerializer
from subcity.api.serializers import SubcitySerializer
from collateralhomefiles.api.serializers import CollateralHomeFilesSerializer
        
class CollateralHomeSerializer(serializers.ModelSerializer):
    homefiles = CollateralHomeFilesSerializer(many=True, read_only=True, required=False)
    hometype = HomeTypeSerializer()
    subcity = SubcitySerializer()
    
    class Meta:
        model = CollateralHome
        fields = '__all__'
        depth = 1

class CollateralHomeSerializerInsert(serializers.ModelSerializer):
    class Meta:
        model = CollateralHome
        fields = '__all__'
