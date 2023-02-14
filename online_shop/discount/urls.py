from django.urls import include, path
from .views import DiscountViewSet


urlpatterns = [
    path('discounts/', CategoryView.as_view({'get':  'retrieve',})),
]