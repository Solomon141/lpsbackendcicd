from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import SpauseDetailSerializer, SpauseDetailSerializerInsert
from spausedetail.models import SpauseDetail

class SpauseDetailList(APIView):
    def get(self, request, format=None):
        SpauseDetails = SpauseDetail.objects.all()
        serializer = SpauseDetailSerializer(SpauseDetails, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpauseDetailSerializerInsert(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SpauseDetailDetail(APIView):
    def get_object(self, pk):
        try:
            return SpauseDetail.objects.get(pk=pk)
        except SpauseDetail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        SpauseDetail = self.get_object(pk)
        serializer = SpauseDetailSerializer(SpauseDetail)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        SpauseDetail = self.get_object(pk)
        serializer = SpauseDetailSerializer(SpauseDetail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        employee = self.get_object(pk)
        serializer = SpauseDetailSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        SpauseDetail = self.get_object(pk)
        SpauseDetail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetSpauseDetailParentID(generics.ListCreateAPIView):
    serializer_class = SpauseDetailSerializer

    def get_queryset(self):
        parent = self.kwargs['parent']
        print("parent")
        print(parent)

        return SpauseDetail.objects.filter(parent = parent)