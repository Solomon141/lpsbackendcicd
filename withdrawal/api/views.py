from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from withdrawal.models import Withdrawal
from .serializers import WithdrawalSerializer, WithdrawalSerializerInsert

class WithdrawalList(APIView):
    def get(self, request):
        sureties = Withdrawal.objects.all()
        serializer = WithdrawalSerializer(sureties, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WithdrawalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WithdrawalDetail(APIView):
    def get_object(self, pk):
        try:
            return Withdrawal.objects.get(pk=pk)
        except Withdrawal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        Withdrawal = self.get_object(pk)
        serializer = WithdrawalSerializerInsert(Withdrawal)
        return Response(serializer.data)

    def put(self, request, pk):
        Withdrawal = self.get_object(pk)
        serializer = WithdrawalSerializer(Withdrawal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        loan = self.get_object(pk)
        serializer = WithdrawalSerializer(loan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Withdrawal = self.get_object(pk)
        Withdrawal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WithdrawByExternalID(generics.ListCreateAPIView):
    serializer_class = WithdrawalSerializer

    def get_queryset(self):
        externalId = self.kwargs['externalId']
        return Withdrawal.objects.filter(externalId = externalId)
    
    
class BulkInsertWithdrawal(generics.CreateAPIView):
    queryset = Withdrawal.objects.all()
    serializer_class = WithdrawalSerializerInsert

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_bulk_create(self, serializer):
        serializer.save()