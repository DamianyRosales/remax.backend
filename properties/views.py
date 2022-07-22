from django.http import Http404, JsonResponse

from properties.helpers import modify_input_for_multiple_files, modify_input_for_multiple_files2
from .serializers import PropertieSerializer, ImageSerializer
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, FileUploadParser
from rest_framework import permissions, status
from .models import Propertie, Image
import operator
from django.db.models import Q
from functools import reduce

# Create your views here.

class PropertieFilterListView(APIView):

    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def post(self, request, **kwars):

        address = request.data['address'] if 'address' in request.data else ''
        typeP = request.data['type'] if 'type' in request.data else ''
        priceGTE = int(request.data['priceGTE']) if 'priceGTE' in request.data else 0
        priceLTE = int(request.data['priceLTE']) if 'priceLTE' in request.data else 2**64 
        sizeGTE = int(request.data['sizeGTE']) if 'sizeGTE' in request.data else 0
        sizeLTE = int(request.data['sizeLTE']) if 'sizeLTE' in request.data else 2**64
        bedrooms = float(request.data['bedrooms']) if 'bedrooms' in request.data else 2**64 
        bathrooms = float(request.data['bathrooms']) if 'bathrooms' in request.data else 2**64 
        parking_lots = int(request.data['parking_lots']) if 'parking_lots' in request.data else 2**64

        #address = self.kwargs['address']
        #typeP = self.kwargs['type']
        #priceGTE = int(self.kwargs['priceGTE'])
        #priceLTE = int(self.kwargs['priceLTE'])
        #sizeGTE = int(self.kwargs['sizeGTE'])
        #sizeLTE = int(self.kwargs['sizeLTE'])
        #bedrooms = float(self.kwargs['bedrooms'])
        #bathrooms = float(self.kwargs['bathrooms'])
        #parking_lots = int(self.kwargs['parking_lots'])

        properties = Propertie.objects.filter(size__gte=sizeGTE, size__lte=sizeLTE, 
                        price__gte=priceGTE, price__lte=priceLTE, bedrooms__lte=bedrooms,
                        parking_lots__lte=parking_lots, bathrooms__lte=bathrooms,
                        address__icontains=address, type__icontains=typeP)
        #properties = Propertie.objects.filter(size__gte=sizeGTE, size__lte=sizeLTE)

        print(properties)

        images = Image.objects.all()
        data = {}
        for i in properties:
            limages = []
            for j in images:
                if j.propertie_id == i.id:
                    n = PropertieSerializer(i)
                    n1 = ImageSerializer(j)
                    limages.append(n1.data)
                    data[n.data['id']] = {'data': n.data, "images": limages}
        return JsonResponse(data=data, status=status.HTTP_200_OK, safe=False)


class PropertieListView(APIView):

    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get(self, request, format=None):
        properties = Propertie.objects.all()
        images = Image.objects.all()
        data = {}
        for i in properties:
            limages = []
            for j in images:
                if j.propertie_id == i.id:
                    n = PropertieSerializer(i)
                    n1 = ImageSerializer(j)
                    limages.append(n1.data)
                    data[n.data['id']] = {'data': n.data, "images": limages}
        return JsonResponse(data=data, status=status.HTTP_200_OK, safe=False)

   
    def put(self, request, address, format=None):
        propertie = self.get_object(address)
        serializer = PropertieSerializer(propertie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        address = request.data['address']
        type = request.data['type']
        price = request.data['price']
        size = request.data['size']
        office = request.data['office']
        bedrooms = request.data['bedrooms']
        bathrooms = request.data['bathrooms']
        parking_lots = request.data['parking_lots']
        lt = request.data['lt']
        ln = request.data['ln']
        description = request.data['description']
        typeOfService = request.data['typeOfService']
        areas = request.data['areas']
        images = dict((request.data).lists())['images']
        arr = []
        preserializer = PropertieSerializer(data=request.data)

        if not preserializer.is_valid():
            return JsonResponse(data=preserializer.errors, status=status.HTTP_400_BAD_REQUEST) 

        for i in images:
            
            propertie_id = Propertie.objects.latest('id').id+1 if Propertie.objects.exists() else 1
            modified_data_image = modify_input_for_multiple_files2(propertie_id=propertie_id,image=i)
            imageUpload = ImageSerializer(data=modified_data_image)
            if imageUpload.is_valid():
                imageUpload.save()
        
                arr.append(imageUpload.data)

        modified_data = modify_input_for_multiple_files(address, type, 
        price, size, office, bedrooms, bathrooms, parking_lots, lt, ln, 
        description, typeOfService, areas, images)
        file_serializer = PropertieSerializer(data=modified_data)
        
        if file_serializer.is_valid():
            file_serializer.save()
            return JsonResponse(data={'propertie':file_serializer.data, 'images': arr}, status=status.HTTP_201_CREATED, safe=False)

        return JsonResponse(data=file_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

