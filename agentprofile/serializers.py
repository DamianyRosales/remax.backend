from rest_framework import serializers
from agentprofile import models

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AgentProfile
        fields = '__all__'

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)
