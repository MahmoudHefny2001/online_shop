from django.urls import include, path
from .views import BrandView, CategoryView, ImageAPIView, ProductView, ProductsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register(r'category', CategoryView),
router.register(r'products', ProductsView),
router.register(r'product', ProductView),
router.register(r'images', ImageAPIView),
# router.register(r'brand', BrandView),

urlpatterns = [
    path('', include(router.urls)),
]