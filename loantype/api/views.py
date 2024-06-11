from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from loantype.models import LoanType
from .serializers import LoanTypeSerializer

class LoanTypeListCreateAPIView(APIView):
    """
    List all loan types or create a new loan type.
    """
    def get(self, request):
        loan_types = LoanType.objects.all()
        serializer = LoanTypeSerializer(loan_types, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LoanTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanTypeDetailAPIView(APIView):
    """
    Retrieve, update or delete a loan type instance.
    """
    def get_object(self, pk):
        try:
            return LoanType.objects.get(pk=pk)
        except LoanType.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        loan_type = self.get_object(pk)
        serializer = LoanTypeSerializer(loan_type)
        return Response(serializer.data)

    def put(self, request, pk):
        loan_type = self.get_object(pk)
        serializer = LoanTypeSerializer(loan_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        loan_type = self.get_object(pk)
        loan_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BulkInsertModel(generics.ListCreateAPIView):
    queryset = LoanType.objects.all()
    serializer_class = LoanTypeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_bulk_create(self, serializer):
        serializer.save()