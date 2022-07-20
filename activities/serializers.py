from activities.models import Trail, Call, Proposal

from rest_framework import serializers

class ActivityTrailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trail
        fields = '__all__'

class ActivityCallSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Call
        fields = '__all__'

class ActivityProposalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Proposal
        fields = '__all__'

