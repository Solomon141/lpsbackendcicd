from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from loancommittee.models import LoanCommittee
from .serializers import LoanCommitteeSerializer, LoanCommitteeSerializerInsert

class LoanCommitteeList(APIView):
    def get(self, request, format=None):
        types = LoanCommittee.objects.all()
        serializer = LoanCommitteeSerializer(types, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LoanCommitteeSerializerInsert(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanCommitteeDetail(APIView):
    def get_object(self, pk):
        try:
            return LoanCommittee.objects.get(pk=pk)
        except LoanCommittee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        home_type = self.get_object(pk)
        serializer = LoanCommitteeSerializer(home_type)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        home_type = self.get_object(pk)
        serializer = LoanCommitteeSerializerInsert(home_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        loan = self.get_object(pk)
        serializer = LoanCommitteeSerializerInsert(loan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        home_type = self.get_object(pk)
        home_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ActiveCommittee(generics.ListCreateAPIView):
    serializer_class = LoanCommitteeSerializer

    def get_queryset(self):
        return LoanCommittee.objects.filter(isActive = True)