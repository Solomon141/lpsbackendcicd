from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from employeedetail.models import EmployeeDetail
from .serializers import EmployeeDetailSerializer, EmployeeDetailSerializerInsert

class EmployeeDetailAPIView(APIView):
    # GET request to retrieve all employee details or create a new one
    def get(self, request):
        employees = EmployeeDetail.objects.all()
        serializer = EmployeeDetailSerializer(employees, many=True)
        return Response(serializer.data)

    # POST request to create a new employee detail
    def post(self, request):
        serializer = EmployeeDetailSerializerInsert(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailDetailAPIView(APIView):
    # Helper method to get an employee instance
    def get_object(self, pk):
        return get_object_or_404(EmployeeDetail, pk=pk)

    # GET request to retrieve a specific employee detail
    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeDetailSerializer(employee)
        return Response(serializer.data)

    # PUT request to update a specific employee detail
    def put(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeDetailSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PATCH request to partially update a specific employee detail
    def patch(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeDetailSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE request to delete a specific employee detail
    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    
class EmployeeDetailUpsertAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        user_id = data.get('user_id')  # Assuming 'user_id' is passed in the request

        if not user_id:
            return Response({'error': 'User ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch the User instance based on the user_id
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Remove the user_id from data as we'll use the 'parent' field directly
        data.pop('user_id', None)
        
        # Use 'parent' as the field for linking to the User model
        employee, created = EmployeeDetail.objects.update_or_create(
            parent=user,  # Use the fetched User instance here
            defaults=data
        )

        serializer = EmployeeDetailSerializer(employee)
        status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK

        return Response(serializer.data, status=status_code)