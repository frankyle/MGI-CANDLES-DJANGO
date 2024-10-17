from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import TraderIdea
from .serializers import TraderIdeaSerializer
from rest_framework.permissions import IsAuthenticated

class TraderIdeaViewSet(viewsets.ModelViewSet):
    queryset = TraderIdea.objects.all()
    serializer_class = TraderIdeaSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data._mutable = True  # Ensure data is mutable before modifying it
        request.data['user'] = request.user.id  # Set the user ID
        serializer = self.get_serializer(data=request.data)  # Remove 'files=request.FILES'

        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
