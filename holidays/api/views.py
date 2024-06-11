from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from holidays.models import Holiday
from .serializers import HolidaySerializer, HolidaySerializerInsert
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
class Holidayviews(ListCreateAPIView):
    serializer_class = HolidaySerializer
    def perform_create(self, serializer):
        return serializer.save()
    
    def get_queryset(self):
        return Holiday.objects.all()
    
class Holidaydetailviews(RetrieveUpdateDestroyAPIView):
    serializer_class = HolidaySerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        return Holiday.objects.all()

class BulkInsertHoliday(generics.CreateAPIView):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializerInsert

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_bulk_create(self, serializer):
        serializer.save()