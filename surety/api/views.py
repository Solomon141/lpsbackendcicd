from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from surety.models import Surety
from .serializers import SuretySerializer

class SuretyList(APIView):
    def get(self, request):
        sureties = Surety.objects.all()
        serializer = SuretySerializer(sureties, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SuretySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SuretyDetail(APIView):
    def get_object(self, pk):
        try:
            return Surety.objects.get(pk=pk)
        except Surety.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        surety = self.get_object(pk)
        serializer = SuretySerializer(surety)
        return Response(serializer.data)

    def put(self, request, pk):
        surety = self.get_object(pk)
        serializer = SuretySerializer(surety, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        loan = self.get_object(pk)
        serializer = SuretySerializer(loan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        surety = self.get_object(pk)
        surety.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
