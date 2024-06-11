from rest_framework import serializers
from employeedetail.models import EmployeeDetail
from authentication.api.serializers import UserSerializer

class EmployeeDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = EmployeeDetail
        fields = '__all__'
        depth = 1

# class ChildEmployeeDetailSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     class Meta:
#         model = EmployeeDetail
#         fields = ['id', 'amFirstname', 'amMiddlename', 'amLastname']
#         depth = 1

class EmployeeDetailSerializerInsert(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetail
        fields = '__all__'