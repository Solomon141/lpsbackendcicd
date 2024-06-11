from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from customercommonfiles.models import CustomerCommonFiles
from .serializers import CustomerCommonFilesSerializer, CustomerCommonFilesSerializerInsert

class CustomerCommonFilesList(APIView):

    queryset = CustomerCommonFiles.objects.all()
    serializer_class = CustomerCommonFilesSerializer


    def get(self, request, format=None):
        files = CustomerCommonFiles.objects.all()
        serializer = CustomerCommonFilesSerializer(files, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerCommonFilesSerializerInsert(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class CustomerCommonFilesDetail(APIView):
    def get_object(self, pk):
        try:
            return CustomerCommonFiles.objects.get(pk=pk)
        except CustomerCommonFiles.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        file = self.get_object(pk)
        serializer = CustomerCommonFilesSerializer(file)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        file = self.get_object(pk)
        serializer = CustomerCommonFilesSerializerInsert(file, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        loan = self.get_object(pk)
        serializer = CustomerCommonFilesSerializerInsert(loan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        file = self.get_object(pk)
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetCheckListByParentID(generics.ListCreateAPIView):
    serializer_class = CustomerCommonFilesSerializer

    def get_queryset(self):
        parent = self.kwargs['parent']

        return CustomerCommonFiles.objects.filter(parent = parent)
    
    
class BulkInsert(generics.CreateAPIView):
    queryset = CustomerCommonFiles.objects.all()
    serializer_class = CustomerCommonFilesSerializerInsert

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_bulk_create(self, serializer):
        serializer.save()
