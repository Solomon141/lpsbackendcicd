from rest_framework import serializers
from loanguaranteepersonfiles.models import LoanGuaranteePersonFiles

class LoanGuaranteePersonFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanGuaranteePersonFiles
        fields = '__all__'
