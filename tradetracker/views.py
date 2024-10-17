from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import TradeTracker  # Import the TradeTracker model
from .serializers import TradeTrackerSerializer  # Import the TradeTracker serializer
from rest_framework.permissions import IsAuthenticated

class TradeTrackerViewSet(viewsets.ModelViewSet):   
    queryset = TradeTracker.objects.all()  # Query all TradeTracker records
    serializer_class = TradeTrackerSerializer  # Use the TradeTracker serializer
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated users

    def create(self, request):
        request.data['user'] = request.user.id  # Automatically associate the logged-in user with the record

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
