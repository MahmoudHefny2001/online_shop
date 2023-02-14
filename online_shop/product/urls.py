from django.urls import include, path
from .views import BrandView, CategoryView, ImageAPIView, ProductView


urlpatterns = [
    path('category/', CategoryView.as_view({'list': 'retrieve', 'read':  'detail',})),
    path('product/', ProductView.as_view({'list': 'retrieve', 'read':  'detail',})),
    path('image/', ImageAPIView.as_view({'list': 'retrieve', 'read':  'detail',})),
    path('brand/', BrandView.as_view({'list': 'retrieve', 'read':  'detail',})),
]