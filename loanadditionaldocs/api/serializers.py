from rest_framework import serializers
from loanadditionaldocs.models import LoanAdditionalFiles

class LoanAdditionalFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanAdditionalFiles
        fields = '__all__'
        depth = 1
        
        
class LoanAdditionalFilesSerializerInsert(serializers.ModelSerializer):
    class Meta:
        model = LoanAdditionalFiles
        fields = '__all__'