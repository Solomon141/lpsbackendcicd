from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from checklist.models import CheckList
from .serializers import CheckListSerializer


class CheckListView(APIView):
    def get(self, request, format=None):
        checklists = CheckList.objects.all()
        serializer = CheckListSerializer(checklists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CheckListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckListDetail(APIView):
    def get_object(self, pk):
        try:
            return CheckList.objects.get(pk=pk)
        except CheckList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        checklist = self.get_object(pk)
        serializer = CheckListSerializer(checklist)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        checklist = self.get_object(pk)
        serializer = CheckListSerializer(checklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        loan = self.get_object(pk)
        serializer = CheckListSerializer(loan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        checklist = self.get_object(pk)
        checklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BulkInsertCkeckList(generics.CreateAPIView):
    queryset = CheckList.objects.all()
    serializer_class = CheckListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_bulk_create(self, serializer):
        serializer.save()

class GetCheckListByParentID(generics.ListCreateAPIView):
    serializer_class = CheckListSerializer

    def get_queryset(self):
        parent = self.kwargs['parent']
        print("parent")
        print(parent)

        return CheckList.objects.filter(parent = parent)