from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from customersingle.models import CustommerSingle
from .serializers import CustommerSingleSerializer, CustommerSingleSerializerInsert

class CustommerSingleList(APIView):
    def get(self, request, format=None):
        items = CustommerSingle.objects.all()
        serializer = CustommerSingleSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustommerSingleSerializerInsert(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustommerSingleDetail(APIView):
    def get_object(self, pk):
        try:
            return CustommerSingle.objects.get(pk=pk)
        except CustommerSingle.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = CustommerSingleSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = CustommerSingleSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        loan = self.get_object(pk)
        serializer = CustommerSingleSerializerInsert(loan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class BulkInsert(generics.CreateAPIView):
    queryset = CustommerSingle.objects.all()
    serializer_class = CustommerSingleSerializerInsert

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_bulk_create(self, serializer):
        serializer.save()
        
        
        
class CustommerSingleDeleteView(APIView):
    def delete(self, request, parent):
        try:
            # parent = CustommerSingle.objects.get(id=parent_id)
            CustommerSingle.objects.filter(parent=parent).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CustommerSingle.DoesNotExist:
            return Response({"error": "Parent not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)