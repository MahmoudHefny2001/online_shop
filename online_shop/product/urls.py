from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import( ProductView, CategoryView, ImageView, BrandView, )

route = DefaultRouter()

route.register(r'category', CategoryView)
route.register(r'brand', BrandView)
route.register(r'product', ProductView)

urlpatterns = [
    path('', include(route.urls)),
]