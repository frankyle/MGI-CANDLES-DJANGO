from rest_framework import serializers
from .models import TradeTracker

class TradeTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeTracker
        fields = '__all__'

    def validate(self, data):
        # Add any custom validation if needed
        return data
