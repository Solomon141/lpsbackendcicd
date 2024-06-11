from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework.decorators import authentication_classes, permission_classes
# from employeedetail.api.serializers import EmployeeDetailSerializer

class UserInGivenGroupSerializer(serializers.ModelSerializer):
    # employees = EmployeeDetailSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        depth = 2



class UserSerializer(serializers.ModelSerializer):
    groups = serializers.CharField(write_only=True)  # Assume group is passed as a name
   
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'groups', 'is_staff'
                  ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        group_name = validated_data.pop('groups', None)
        # user = User.objects.create_user(**validated_data)
        user = User.objects.create_user(validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
            is_staff=True)
        
        # Assign group
        if group_name:
            group, created = Group.objects.get_or_create(name=group_name)  # Use your group model if custom
            user.groups.add(group)
        
        return user
    

class UserSerializerLogin(serializers.ModelSerializer):
    groups = serializers.StringRelatedField(write_only=False, many=True)  # Assume group is passed as a name
   
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'groups', 'is_staff'
                  ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        group_name = validated_data.pop('groups', None)
        # user = User.objects.create_user(**validated_data)
        user = User.objects.create_user(validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
            is_staff=True)
        
        # Assign group
        if group_name:
            group, created = Group.objects.get_or_create(name=group_name)  # Use your group model if custom
            user.groups.add(group)
        
        return user
    
@authentication_classes([])
@permission_classes([])
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    username = serializers.CharField(max_length=255, min_length=2)
    groups = serializers.StringRelatedField(write_only=False, many=True)  # Assume group is passed as a name

    class Meta:
        model = User
        fields = '__all__'
        depth = 1
        eextra_kwargs = {'password': {'write_only': True}}