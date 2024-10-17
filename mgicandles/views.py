from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import MgiCandles
from .serializers import MgiCandlesSerializer
from rest_framework.permissions import IsAuthenticated

class MgiCandlesViewSet(viewsets.ModelViewSet):
    queryset = MgiCandles.objects.all()
    serializer_class = MgiCandlesSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        request.data['user'] = request.user.id

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
