from rest_framework import serializers
from loancomment.models import LoanComment
from authentication.api.serializers import UserSerializer

class LoanCommentSerializer(serializers.ModelSerializer):
    commentedBy = UserSerializer()
    class Meta:
        model = LoanComment
        fields = '__all__'


class LoanCommentSerializerInsert(serializers.ModelSerializer):
    class Meta:
        model = LoanComment
        fields = '__all__'