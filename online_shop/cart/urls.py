from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'my-cart', views.CartAPIView)

urlpatterns = [
    path('', include(router.urls)),
]