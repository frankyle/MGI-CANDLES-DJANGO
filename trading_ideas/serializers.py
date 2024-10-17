from rest_framework import serializers
from .models import TraderIdea

class TraderIdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TraderIdea
        fields = '__all__'  # This will include all the fields from the model
