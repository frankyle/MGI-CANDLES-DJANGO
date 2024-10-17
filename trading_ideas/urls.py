from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TraderIdeaViewSet

router = DefaultRouter()
router.register(r'traderideas', TraderIdeaViewSet, basename='traderidea')

urlpatterns = [
    path('', include(router.urls)),
]
