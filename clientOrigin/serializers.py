from clientOrigin.models import ClientOrigin

from rest_framework import serializers

class OriginSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientOrigin
        fields = '__all__'

