from django.http import Http404, JsonResponse
from officesLocations.serializers import OfficeSerializer
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, FileUploadParser
from rest_framework import permissions, status
from .models import Office

# Create your views here.

class OfficeListView(APIView):

    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get(self, request, format=None):
        offices = Office.objects.all()
        serializer = OfficeSerializer(offices, many=True)
        return JsonResponse(data=serializer.data, status=status.HTTP_200_OK, safe=False)

    def post(self, request, format=None):
        serializer = OfficeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
