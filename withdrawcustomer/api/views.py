from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from withdrawcustomer.models import WithdrawCustomer
from .serializers import WithdrawCustomerSerializer

class WithdrawCustomerList(APIView):
    def get(self, request):
        WithdrawCustomers = WithdrawCustomer.objects.all()
        serializer = WithdrawCustomerSerializer(WithdrawCustomers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WithdrawCustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WithdrawCustomerDetail(APIView):
    def get_object(self, pk):
        try:
            return WithdrawCustomer.objects.get(pk=pk)
        except WithdrawCustomer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        WithdrawCustomer = self.get_object(pk)
        serializer = WithdrawCustomerSerializer(WithdrawCustomer)
        return Response(serializer.data)

    def put(self, request, pk):
        WithdrawCustomer = self.get_object(pk)
        serializer = WithdrawCustomerSerializer(WithdrawCustomer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        loan = self.get_object(pk)
        serializer = WithdrawCustomerSerializer(loan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        WithdrawCustomer = self.get_object(pk)
        WithdrawCustomer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetUserByExternalID(generics.ListAPIView):
    serializer_class = WithdrawCustomerSerializer
    def get_queryset(self):
        entityExternalId = self.kwargs['entityExternalId']
        print(entityExternalId)
        return WithdrawCustomer.objects.filter(entityExternalId = entityExternalId)
    
class GetUserByFineractCustID(generics.ListAPIView):
    serializer_class = WithdrawCustomerSerializer

    def get_queryset(self):
        entityAccountNo = self.kwargs['entityAccountNo']
        return WithdrawCustomer.objects.filter(entityAccountNo = entityAccountNo)