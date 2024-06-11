from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from loanguaranteeperson.models import LoanGuaranteePerson
from .serializers import LoanGuaranteePersonSerializer, LoanGuaranteePersonSerializerInsert
from .serializers import LoanGuaranteePersonSerializerSelect

class LoanGuaranteePersonList(APIView):
    """
    List all loan guarantee persons, or create a new one.
    """
    def get(self, request, format=None):
        loan_guarantee_persons = LoanGuaranteePerson.objects.all()
        serializer = LoanGuaranteePersonSerializer(loan_guarantee_persons, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LoanGuaranteePersonSerializerInsert(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanGuaranteePersonDetail(APIView):
    """
    Retrieve, update or delete a loan guarantee person instance.
    """
    def get_object(self, pk):
        try:
            return LoanGuaranteePerson.objects.get(pk=pk)
        except LoanGuaranteePerson.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        loan_guarantee_person = self.get_object(pk)
        serializer = LoanGuaranteePersonSerializer(loan_guarantee_person)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        loan_guarantee_person = self.get_object(pk)
        serializer = LoanGuaranteePersonSerializer(loan_guarantee_person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        loan_guarantee_person = self.get_object(pk)
        serializer = LoanGuaranteePersonSerializer(loan_guarantee_person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
           
    def delete(self, request, pk, format=None):
        loan_guarantee_person = self.get_object(pk)
        loan_guarantee_person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetGuaranteePersonByLoanID(generics.ListCreateAPIView):
    serializer_class = LoanGuaranteePersonSerializer

    def get_queryset(self):
        loan = self.kwargs['loan']
        print("loan")
        print(loan)

        return LoanGuaranteePerson.objects.filter(loan = loan)