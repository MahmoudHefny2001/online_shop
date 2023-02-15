from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import OrderViewSet, OrderAPIView


router = DefaultRouter()
router.register(r'my-orders', OrderAPIView)
router.register(r'make-order', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]