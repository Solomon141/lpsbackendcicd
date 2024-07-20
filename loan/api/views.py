from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from loan.models import Loan
from .serializers import LoanSerializer, LoanSerializerInsert
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
class LoanList(APIView):
    
    @swagger_auto_schema(
        operation_description="This is Wow Description of your list/create API endpoint",
        responses={200: LoanSerializer(many=True)}
    )
    def get(self, request):
        loans = Loan.objects.all()
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LoanSerializerInsert(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoanDetail(APIView):
    def get_object(self, pk):
        try:
            return Loan.objects.get(pk=pk)
        except Loan.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        loan = get_object_or_404(Loan, pk=pk)
        serializer = LoanSerializer(loan)
        return Response(serializer.data)

    def put(self, request, pk):
        loan = get_object_or_404(Loan, pk=pk)
        serializer = LoanSerializer(loan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        loan = self.get_object(pk)
        serializer = LoanSerializerInsert(loan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        loan = get_object_or_404(Loan, pk=pk)
        loan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class loanByOfficerID(generics.ListCreateAPIView):
    serializer_class = LoanSerializer

    def get_queryset(self):
        officerid = self.kwargs['officerid']
        print("officerid")
        print(officerid)

        return Loan.objects.filter(submittedBy = officerid)
    
class AssignedToIfNotNull():
    pass