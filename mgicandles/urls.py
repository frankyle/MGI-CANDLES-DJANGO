from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MgiCandlesViewSet  

router = DefaultRouter()
router.register(r'mgicandles', MgiCandlesViewSet, basename='mgicandle')  # Use a basename for consistency

urlpatterns = [
    path('', include(router.urls)),  # No additional path here
]

  