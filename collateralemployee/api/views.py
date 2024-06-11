from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from collateralemployee.models import Collateral_Employee
from .serializers import CollateralEmployeeSerializer, CollateralEmployeeSerializerInsert

class CollateralEmployeeList(APIView):
    """
    List all employees, or create a new employee.
    """
    def get(self, request, format=None):
        employees = Collateral_Employee.objects.all()
        serializer = CollateralEmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CollateralEmployeeSerializerInsert(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CollateralEmployeeDetail(APIView):
    """
    Retrieve, update or delete a employee instance.
    """
    def get_object(self, pk):
        try:
            return Collateral_Employee.objects.get(pk=pk)
        except Collateral_Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = CollateralEmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = CollateralEmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = CollateralEmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetSalaryCollateralByLoanID(generics.ListCreateAPIView):
    serializer_class = CollateralEmployeeSerializer

    def get_queryset(self):
        loan = self.kwargs['loan']
        print("loan")
        print(loan)

        return Collateral_Employee.objects.filter(loan = loan)