from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import( ProductView, CategoryView, ImageAPIView, BrandView, )


urlpatterns = [
    path('category/', CategoryView.as_view({'get': 'retrieve', 'get':  'detail',})),
    path('product/', ProductView.as_view({'get': 'retrieve', 'get':  'detail',})),
    path('image/', ImageAPIView.as_view({'get': 'retrieve', 'get':  'detail',})),
    path('brand/', BrandView.as_view({'get': 'retrieve', 'get':  'detail',})),
]