from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from collateralcar.models import Collateral_Car
from .serializers import CollateralCarSerializer, CollateralCarSerializerInsert

class CollateralCarList(APIView):
    def get(self, request, format=None):
        cars = Collateral_Car.objects.all()
        serializer = CollateralCarSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CollateralCarSerializerInsert(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    # steps 
    # check if response is valid and 
    # select all related checklists from checklist app where parent = 6
    # then post bulk insert into carcommonfiles

class CollateralCarDetail(APIView):
    def get_object(self, pk):
        try:
            return Collateral_Car.objects.get(pk=pk)
        except Collateral_Car.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = CollateralCarSerializer(car)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = CollateralCarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        car = self.get_object(pk)
        serializer = CollateralCarSerializerInsert(car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        car = self.get_object(pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class GetSalaryCollateralByLoanID(generics.ListCreateAPIView):
#     serializer_class = CollateralCarSerializer

#     def get_queryset(self):
#         loan = self.kwargs['loan']
#         print("loan")
#         print(loan)

#         return Collateral_Car.objects.filter(loan = loan)