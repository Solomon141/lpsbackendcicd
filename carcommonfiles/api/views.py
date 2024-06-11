from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from carcommonfiles.models import Car_Files
from .serializers import CarFilesSerializer

class CarFilesList(APIView):

    queryset = Car_Files.objects.all()
    serializer_class = CarFilesSerializer


    def get(self, request, format=None):
        files = Car_Files.objects.all()
        serializer = CarFilesSerializer(files, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarFilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class CarFilesDetail(APIView):
    def get_object(self, pk):
        try:
            return Car_Files.objects.get(pk=pk)
        except Car_Files.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        file = self.get_object(pk)
        serializer = CarFilesSerializer(file)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        file = self.get_object(pk)
        serializer = CarFilesSerializer(file, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        loan = self.get_object(pk)
        serializer = CarFilesSerializer(loan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        file = self.get_object(pk)
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class BulkInsert(generics.CreateAPIView):
    queryset = Car_Files.objects.all()
    serializer_class = CarFilesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_bulk_create(self, serializer):
        serializer.save()