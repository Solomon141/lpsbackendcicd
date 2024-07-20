from .serializers import UserSerializer, LoginSerializer, UserSerializerLogin
from .serializers import UserInGivenGroupSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User, Group
from rest_framework import generics
from django.contrib import auth
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

# Create your views here.
class UsersInGroup_OFFICERS(APIView):
    def get(self, request):
        # group = Group.objects.get(name=group_name)
        group = Group.objects.get(name="ROLE_OFFICER")
        
        users = User.objects.filter(groups=group)
        serializer = UserInGivenGroupSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class ALL_USERS(APIView):
    def get(self, request):
        users = User.objects.filter()
        serializer = UserSerializerLogin(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    

class BulkUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_bulk_create(self, serializer):
        serializer.save()


    
class LoginView(GenericAPIView):
    permission_classes = ()
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')

        user = auth.authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            auth_token =  {    'refresh': str(refresh),    'access': str(refresh.access_token),}

            serializer = UserSerializerLogin(user)
            data = {'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)
            # SEND RES
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    
    

class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = LoginSerializer(car)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = LoginSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        loan = self.get_object(pk)
        serializer = LoginSerializer(loan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
