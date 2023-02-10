from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import( ProductView, CategoryView, ImageView, BrandView, )

route = DefaultRouter()

route.register(r'Category', CategoryView)
route.register(r'Brand', BrandView)
route.register(r'Product', ProductView)

urlpatterns = [
    path('', include(route.urls)),
]