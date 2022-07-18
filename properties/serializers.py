from properties.models import Propertie

from rest_framework import serializers

class PropertieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Propertie
        fields = '__all__'

