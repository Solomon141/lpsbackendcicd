from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from withdrawaldetail.models import WithdrawalDetail
from .serializers import WithdrawalDetailSerializer, WithdrawalDetailSerializerInsert

class WithdrawalDetailList(APIView):
    def get(self, request):
        sureties = WithdrawalDetail.objects.all()
        serializer = WithdrawalDetailSerializer(sureties, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WithdrawalDetailSerializerInsert(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WithdrawalDetailDetail(APIView):
    def get_object(self, pk):
        try:
            return WithdrawalDetail.objects.get(pk=pk)
        except WithdrawalDetail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        WithdrawalDetail = self.get_object(pk)
        serializer = WithdrawalDetailSerializer(WithdrawalDetail)
        return Response(serializer.data)

    def put(self, request, pk):
        WithdrawalDetail = self.get_object(pk)
        serializer = WithdrawalDetailSerializer(WithdrawalDetail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        loan = self.get_object(pk)
        serializer = WithdrawalDetailSerializer(loan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        WithdrawalDetail = self.get_object(pk)
        WithdrawalDetail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WithdrawByExternalID(generics.ListCreateAPIView):
    serializer_class = WithdrawalDetailSerializer

    def get_queryset(self):
        externalId = self.kwargs['externalId']
        return WithdrawalDetail.objects.filter(externalId = externalId)