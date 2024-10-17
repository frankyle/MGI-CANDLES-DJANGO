from rest_framework import serializers
from .models import MgiCandles

class MgiCandlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MgiCandles
        fields = '__all__'

    def validate(self, data):
        # Custom validation logic if necessary
        return data
