from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from collateralhome.models import CollateralHome
from .serializers import CollateralHomeSerializer, CollateralHomeSerializerInsert

class CollateralHomeList(APIView):
    def get(self, request, format=None):
        homes = CollateralHome.objects.all()
        serializer = CollateralHomeSerializer(homes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CollateralHomeSerializerInsert(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CollateralHomeDetail(APIView):
    def get_object(self, pk):
        try:
            return CollateralHome.objects.get(pk=pk)
        except CollateralHome.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        home = self.get_object(pk)
        serializer = CollateralHomeSerializer(home)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        home = self.get_object(pk)
        serializer = CollateralHomeSerializer(home, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        home = self.get_object(pk)
        serializer = CollateralHomeSerializerInsert(home, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        home = self.get_object(pk)
        home.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
