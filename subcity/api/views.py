from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from subcity.models import Subcity
from .serializers import SubcitySerializer, SubcitySerializerInsert

class SubcityList(APIView):
    def get(self, request, format=None):
        Subcitys = Subcity.objects.all()
        serializer = SubcitySerializer(Subcitys, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubcitySerializerInsert(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubcityDetail(APIView):
    def get_object(self, pk):
        try:
            return Subcity.objects.get(pk=pk)
        except Subcity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        Subcity = self.get_object(pk)
        serializer = SubcitySerializer(Subcity)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Subcity = self.get_object(pk)
        serializer = SubcitySerializer(Subcity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        employee = self.get_object(pk)
        serializer = SubcitySerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Subcity = self.get_object(pk)
        Subcity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BulkInsertSubcity(generics.CreateAPIView):
    queryset = Subcity.objects.all()
    serializer_class = SubcitySerializerInsert

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_bulk_create(self, serializer):
        serializer.save()