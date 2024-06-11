from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from hometype.models import HomeType
from .serializers import HomeTypeSerializer

class HomeTypeList(APIView):
    def get(self, request, format=None):
        types = HomeType.objects.all()
        serializer = HomeTypeSerializer(types, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HomeTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HomeTypeDetail(APIView):
    def get_object(self, pk):
        try:
            return HomeType.objects.get(pk=pk)
        except HomeType.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        home_type = self.get_object(pk)
        serializer = HomeTypeSerializer(home_type)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        home_type = self.get_object(pk)
        serializer = HomeTypeSerializer(home_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        loan = self.get_object(pk)
        serializer = HomeTypeSerializer(loan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        home_type = self.get_object(pk)
        home_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BulkInsertModel(generics.ListCreateAPIView):
    queryset = HomeType.objects.all()
    serializer_class = HomeTypeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_bulk_create(self, serializer):
        serializer.save()