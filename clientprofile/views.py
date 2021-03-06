from django.http import Http404, JsonResponse
from clientprofile.serializers import ClientSerializer
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, FileUploadParser
from rest_framework import permissions, status
from .models import ClientProfile
import json

# Create your views here.

class Client_view_post(APIView):
    
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def put(self, request, pk=None):
        data = json.loads(json.dumps(request.data))

        for i in ClientProfile.objects.all():
            if i.email == request.data.get('email'):
                email = i.email

                client = ClientProfile.objects.get(email=email)

                serializer = ClientSerializer(client, data=data)

                if serializer.is_valid():
                    serializer.save()

                    return JsonResponse(data=serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        data = json.loads(json.dumps(request.data))
        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            
            serializer.save()
            self.put(request)

            return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientList_view(APIView):

    # permission_classes = [permissions.AllowAny]
    
    parser_classes = (JSONParser, FormParser, MultiPartParser, FileUploadParser)

    def get(self, request, format = None):
        clients = ClientProfile.objects.all()
        serializer = ClientSerializer(clients, many = True)

        return JsonResponse(data=serializer.data, safe = False)


    def post(self, request, format = None):
        
        serializer = ClientSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return JsonResponse(data=serializer.data, status = status.HTTP_201_CREATED)
        
        return JsonResponse(data=serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ClientDetail_view(APIView):
    # permission_classes = [permissions.AllowAny]
    parser_classes = (JSONParser, FormParser, MultiPartParser, FileUploadParser)

    def get_object(self, pk):
        try:
            return ClientProfile.objects.get(pk = pk)
        except ClientProfile.DoesNotExist:
            raise Http404

    def get(self, pk, request, format = None):
        client = self.get_object(pk = pk)
        serializer = ClientSerializer(client)

        return JsonResponse(data=serializer.data, safe = False)


    def put(self, request, pk, format=None):

        client = self.get_object(pk = pk)
        serializer = ClientSerializer(client, data = request.data)

        if serializer.is_valid():
            serializer.save()
            
            return JsonResponse(data=serializer.data, status = status.HTTP_200_OK)
        
        return JsonResponse(data=serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format = None):
        client = self.get_object(pk = pk)
        serializer = ClientSerializer(client)
        client.delete()
        sd = serializer.data
        sd['id'] = pk

        return JsonResponse(data=sd, safe=False) 

