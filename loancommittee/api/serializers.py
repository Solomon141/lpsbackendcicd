from rest_framework import serializers
from loancommittee.models import LoanCommittee
from jobposition.api.serializers import JonbPositionSerializer

class LoanCommitteeSerializer(serializers.ModelSerializer):
    jobposition = JonbPositionSerializer()
    class Meta:
        model = LoanCommittee
        fields = '__all__'