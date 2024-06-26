from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from delegation.models import Delegation
from .serializers import DelegationSerializer, DelegationSerializerInsert

class DelegationList(APIView):
    def get(self, request):
        sureties = Delegation.objects.all()
        serializer = DelegationSerializer(sureties, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DelegationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DelegationDetail(APIView):
    def get_object(self, pk):
        try:
            return Delegation.objects.get(pk=pk)
        except Delegation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        Delegation = self.get_object(pk)
        serializer = DelegationSerializer(Delegation)
        return Response(serializer.data)

    def put(self, request, pk):
        Delegation = self.get_object(pk)
        serializer = DelegationSerializer(Delegation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        loan = self.get_object(pk)
        serializer = DelegationSerializer(loan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Delegation = self.get_object(pk)
        Delegation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetDelegationByLoanID(generics.ListCreateAPIView):
    serializer_class = DelegationSerializer

    def get_queryset(self):
        loan = self.kwargs['loan']
        print("loan")
        print(loan)

        return Delegation.objects.filter(loan = loan)