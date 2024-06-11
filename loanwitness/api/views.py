from rest_framework.views import APIView
from rest_framework.response import Response
from loanwitness.models import LoanWitness
from .serializers import LoanWitnessSerializer
from rest_framework import status, generics

class LoanWitnessList(APIView):
    def get(self, request):
        sureties = LoanWitness.objects.all()
        serializer = LoanWitnessSerializer(sureties, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LoanWitnessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanWitnessDetail(APIView):
    def get_object(self, pk):
        try:
            return LoanWitness.objects.get(pk=pk)
        except LoanWitness.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        LoanWitness = self.get_object(pk)
        serializer = LoanWitnessSerializer(LoanWitness)
        return Response(serializer.data)

    def put(self, request, pk):
        LoanWitness = self.get_object(pk)
        serializer = LoanWitnessSerializer(LoanWitness, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        loan = self.get_object(pk)
        serializer = LoanWitnessSerializer(loan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        LoanWitness = self.get_object(pk)
        LoanWitness.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetWitnessByLoanID(generics.ListCreateAPIView):
    serializer_class = LoanWitnessSerializer

    def get_queryset(self):
        loan = self.kwargs['loan']
        print("loan")
        print(loan)

        return LoanWitness.objects.filter(loan = loan)