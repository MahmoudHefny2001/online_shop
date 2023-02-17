from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import OrderItemViewSet, OrderViewSet



router = DefaultRouter()

router.register(r'^(?P<order_id>\d+)/order-items', OrderItemViewSet)
router.register(r'', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]