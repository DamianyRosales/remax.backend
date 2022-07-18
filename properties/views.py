from django.http import Http404, JsonResponse
from .serializers import PropertieSerializer
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, FileUploadParser
from rest_framework import permissions, status
from .models import Propertie

# Create your views here.

class PropertieListView(APIView):

    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get(self, request, format=None):
        properties = Propertie.objects.all()
        serializer = PropertieSerializer(properties, many=True)
        return JsonResponse(data=serializer.data, status=status.HTTP_200_OK, safe=False)

    def post(self, request, format=None):
        serializer = PropertieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
