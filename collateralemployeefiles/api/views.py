from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from collateralemployeefiles.models import Collateral_EmployeeFiles
from .serializers import CollateralEmployeeFilesSerializer


class CollateralEmployeeFilesList(APIView):
    def get(self, request, format=None):
        collateral_files = Collateral_EmployeeFiles.objects.all()
        serializer = CollateralEmployeeFilesSerializer(collateral_files, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CollateralEmployeeFilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CollateralEmployeeFilesDetail(APIView):
    def get_object(self, pk):
        try:
            return Collateral_EmployeeFiles.objects.get(pk=pk)
        except Collateral_EmployeeFiles.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        collateral_file = self.get_object(pk)
        serializer = CollateralEmployeeFilesSerializer(collateral_file)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        collateral_file = self.get_object(pk)
        serializer = CollateralEmployeeFilesSerializer(collateral_file, data=request.data, partial=True) # partial=True allows partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        collateral_file = self.get_object(pk)
        collateral_file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BulkInsert(generics.CreateAPIView):
    queryset = Collateral_EmployeeFiles.objects.all()
    serializer_class = CollateralEmployeeFilesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_bulk_create(self, serializer):
        serializer.save()