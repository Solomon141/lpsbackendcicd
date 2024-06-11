from rest_framework import serializers
from loanwitness.models import LoanWitness

class LoanWitnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanWitness
        fields = '__all__'
