from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework import permissions
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, FileUploadParser
from rest_framework.response import Response

from agentprofile import models
from agentprofile.serializers import AgentSerializer

import json

# Create your views here.

class agent_view_post(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def put(self, request, pk=None):
        data = json.loads(json.dumps(request.data))

        for i in models.AgentProfile.objects.all():
            if i.email == request.data.get('email'):
                email = i.email

                agent = models.AgentProfile.objects.get(email=email)

                serializer = AgentSerializer(agent, data=data)

                if serializer.is_valid():
                    serializer.save()

                    return JsonResponse(data=serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        data = json.loads(json.dumps(request.data))
        serializer = AgentSerializer(data=data)
        if serializer.is_valid():
            
            serializer.save()
            self.put(request)

            return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class agent_view(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get(self, request=None, format=None):

        agents = models.AgentProfile.objects.all()
        serializer = AgentSerializer(agents, many=True)
        
        return JsonResponse(data=serializer.data, safe=False)

    
    def put(self, request, pk=None):
        data = request.data
        data = json.loads(json.dumps(request.data))
        
        
        for i in models.AgentProfile.objects.all():
            if i.email == request.data.get('email'):
                email = i.email

        agent = models.AgentProfile.objects.get(email=email)

        serializer = AgentSerializer(agent, data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(data=serializer.data)

    def delete(self, request, format=None):
        for i in models.AgentSerializer.objects.all():
            if i.email == request.data.get('email'):
                email = i.email

                agent = models.AgentProfile.objects.get(email=email)
                agent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class States(APIView):
    
    def get(self, request):
        mexican_states = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche",
            "Chiapas", "Chihuahua", "Coahuila de Zaragoza", "Colima", "Ciudad de México",
            "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "Estado de Mexico", "Michoacan de Ocampo",
            "Morelos", "Nayarit", "Nuevo Leon", "Oaxaca", "Puebla", "Queretaro de Arteaga",
            "Quintana Roo", "San Luis Potosi", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas",
            "Tlaxcala", "Veracruz de Ignacio de la Llave", "Yucatan", "Zacatecas",]
        permission_classes = [permissions.AllowAny]
        authentication_classes = []
        parser_classes = (MultiPartParser, FormParser, JSONParser)
        
        return JsonResponse(data = json.dumps(mexican_states))
