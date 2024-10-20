from django.shortcuts import render
from django.http import JsonResponse
from api.models import User

from api.serializer import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import TokenError

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError

from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.exceptions import AuthenticationFailed

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            return response
        except TokenError as e:
            return Response({"detail": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        except InvalidToken as e:
            return Response({"detail": "Invalid credentials. Please try again."}, status=status.HTTP_401_UNAUTHORIZED)
        except AuthenticationFailed as e:
            return Response({"detail": "Authentication failed."}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            # Catch any other unexpected errors
            return Response({"detail": "An error occurred during login."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            # Add debugging log
            print("User registered successfully.")
            return response
        except ValidationError as e:
            # Catch validation errors and return a proper response
            print(f"Validation Error: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Add more logging for unexpected exceptions
            print(f"Unexpected error: {str(e)}")
            return Response({"error": "Registration failed. Please try again."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Get All Routes

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/'
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = "Hello buddy"
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)