from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from carmanufacturer.models import Car_Manufacture
from .serializers import CarManufactureSerializer

class CarManufactureList(APIView):
    def get(self, request, format=None):
        manufactures = Car_Manufacture.objects.all()
        serializer = CarManufactureSerializer(manufactures, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarManufactureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarManufactureDetail(APIView):
    def get_object(self, pk):
        try:
            return Car_Manufacture.objects.get(pk=pk)
        except Car_Manufacture.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        manufacture = self.get_object(pk)
        serializer = CarManufactureSerializer(manufacture)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        manufacture = self.get_object(pk)
        serializer = CarManufactureSerializer(manufacture, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        loan = self.get_object(pk)
        serializer = CarManufactureSerializer(loan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        manufacture = self.get_object(pk)
        manufacture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BulkInsertManufacture(generics.ListCreateAPIView):
    queryset = Car_Manufacture.objects.all()
    serializer_class = CarManufactureSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_bulk_create(self, serializer):
        serializer.save()