from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from loanadditionaldocs.models import LoanAdditionalFiles
from .serializers import LoanAdditionalFilesSerializer, LoanAdditionalFilesSerializerInsert

class LoanAdditionalFilesList(APIView):

    queryset = LoanAdditionalFiles.objects.all()
    serializer_class = LoanAdditionalFilesSerializer


    def get(self, request, format=None):
        files = LoanAdditionalFiles.objects.all()
        serializer = LoanAdditionalFilesSerializer(files, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LoanAdditionalFilesSerializerInsert(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class LoanAdditionalFilesDetail(APIView):
    def get_object(self, pk):
        try:
            return LoanAdditionalFiles.objects.get(pk=pk)
        except LoanAdditionalFiles.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        file = self.get_object(pk)
        serializer = LoanAdditionalFilesSerializer(file)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        file = self.get_object(pk)
        serializer = LoanAdditionalFilesSerializerInsert(file, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        loan = self.get_object(pk)
        serializer = LoanAdditionalFilesSerializerInsert(loan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        file = self.get_object(pk)
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetCheckListByParentID(generics.ListCreateAPIView):
    serializer_class = LoanAdditionalFilesSerializer

    def get_queryset(self):
        parent = self.kwargs['parent']

        return LoanAdditionalFiles.objects.filter(parent = parent)
    
    
class BulkInsert(generics.CreateAPIView):
    queryset = LoanAdditionalFiles.objects.all()
    serializer_class = LoanAdditionalFilesSerializerInsert

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_bulk_create(self, serializer):
        serializer.save()
