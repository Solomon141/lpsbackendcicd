from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from checklisttype.models import CheckListType
from .serializers import CheckListTypeSerializer, CheckListTypeSerializerInsert

class CheckListTypeList(APIView):
    def get(self, request, format=None):
        checklisttypes = CheckListType.objects.all()
        serializer = CheckListTypeSerializer(checklisttypes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CheckListTypeSerializerInsert(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckListTypeDetail(APIView):
    def get_object(self, pk):
        try:
            return CheckListType.objects.get(pk=pk)
        except CheckListType.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        checklisttype = self.get_object(pk)
        serializer = CheckListTypeSerializer(checklisttype)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        checklisttype = self.get_object(pk)
        serializer = CheckListTypeSerializer(checklisttype, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        employee = self.get_object(pk)
        serializer = CheckListTypeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        checklisttype = self.get_object(pk)
        checklisttype.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BulkInsertCheckListType(generics.CreateAPIView):
    queryset = CheckListType.objects.all()
    serializer_class = CheckListTypeSerializerInsert

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_bulk_create(self, serializer):
        serializer.save()