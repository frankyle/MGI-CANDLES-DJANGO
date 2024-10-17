from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TradeTrackerViewSet  # Import the TradeTrackerViewSet

router = DefaultRouter()
router.register(r'tradetracker', TradeTrackerViewSet, basename='tradetracker')  # Register the TradeTracker route

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs in the main path
]
