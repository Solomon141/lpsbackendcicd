from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from customer.models import Customer
from .serializers import CustomerSerializer

class CustomerList(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetail(APIView):
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        loan = self.get_object(pk)
        serializer = CustomerSerializer(loan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetUserByExternalID(generics.ListAPIView):
    serializer_class = CustomerSerializer
    def get_queryset(self):
        entityExternalId = self.kwargs['entityExternalId']
        print(entityExternalId)
        return Customer.objects.filter(entityExternalId = entityExternalId)
    
class GetUserByFineractCustID(generics.ListAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        entityAccountNo = self.kwargs['entityAccountNo']
        return Customer.objects.filter(entityAccountNo = entityAccountNo)