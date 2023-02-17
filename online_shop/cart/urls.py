from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.response import Response

router = DefaultRouter()

router.register(r'', views.CartAPIView)
router.register(r'my-cart', views.CartAPIView)
router.register(r'cart-edit', views.CartViewSet)


urlpatterns = [
    path('', include(router.urls)),
]