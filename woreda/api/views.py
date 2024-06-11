from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from woreda.models import Woreda
from .serializers import WoredaSerializer

class WoredaView(APIView):
    def get(self, request, format=None):
        Woredas = Woreda.objects.all()
        serializer = WoredaSerializer(Woredas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WoredaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WoredaDetail(APIView):
    def get_object(self, pk):
        try:
            return Woreda.objects.get(pk=pk)
        except Woreda.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        Woreda = self.get_object(pk)
        serializer = WoredaSerializer(Woreda)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Woreda = self.get_object(pk)
        serializer = WoredaSerializer(Woreda, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        loan = self.get_object(pk)
        serializer = WoredaSerializer(loan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Woreda = self.get_object(pk)
        Woreda.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BulkInsertCkeckList(generics.CreateAPIView):
    queryset = Woreda.objects.all()
    serializer_class = WoredaSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_bulk_create(self, serializer):
        serializer.save()

class GetWoredaByParentID(generics.ListCreateAPIView):
    serializer_class = WoredaSerializer

    def get_queryset(self):
        parent = self.kwargs['parent']
        print("parent")
        print(parent)

        return Woreda.objects.filter(parent = parent)