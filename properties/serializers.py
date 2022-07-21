from properties.models import Image, Propertie

from rest_framework import serializers

class PropertieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Propertie
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Image
        fields = '__all__'
