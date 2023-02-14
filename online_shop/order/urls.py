from django.urls import path, include
from .view import OrderViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'my-order', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]