from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from loanguaranteepersonfiles.models import LoanGuaranteePersonFiles
from .serializers import LoanGuaranteePersonFilesSerializer

class LoanGuaranteePersonFilesList(APIView):
    """
    List all loan guarantee person files, or create a new one.
    """
    def get(self, request, format=None):
        files = LoanGuaranteePersonFiles.objects.all()
        serializer = LoanGuaranteePersonFilesSerializer(files, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LoanGuaranteePersonFilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanGuaranteePersonFilesDetail(APIView):
    """
    Retrieve, update or delete a loan guarantee person file instance.
    """
    def get_object(self, pk):
        try:
            return LoanGuaranteePersonFiles.objects.get(pk=pk)
        except LoanGuaranteePersonFiles.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        file = self.get_object(pk)
        serializer = LoanGuaranteePersonFilesSerializer(file)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        file = self.get_object(pk)
        serializer = LoanGuaranteePersonFilesSerializer(file, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        file = self.get_object(pk)
        serializer = LoanGuaranteePersonFilesSerializer(file, data=request.data, partial=True) # Notice the `partial=True`
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        file = self.get_object(pk)
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
