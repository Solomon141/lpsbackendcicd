from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from collateralstock.models import CollateralStock
from .serializers import CollateralStockSerializer, CollateralStockSerializerInsert

class CollateralStockList(APIView):
    def get(self, request, format=None):
        homes = CollateralStock.objects.all()
        serializer = CollateralStockSerializer(homes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CollateralStockSerializerInsert(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CollateralStockDetail(APIView):
    def get_object(self, pk):
        try:
            return CollateralStock.objects.get(pk=pk)
        except CollateralStock.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        home = self.get_object(pk)
        serializer = CollateralStockSerializer(home)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        home = self.get_object(pk)
        serializer = CollateralStockSerializer(home, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        home = self.get_object(pk)
        serializer = CollateralStockSerializerInsert(home, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        home = self.get_object(pk)
        home.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetStockCollateralByLoanID(generics.ListCreateAPIView):
    serializer_class = CollateralStockSerializer

    def get_queryset(self):
        loan = self.kwargs['loan']
        return CollateralStock.objects.filter(loan = loan)