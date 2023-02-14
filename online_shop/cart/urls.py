from django.urls import include, path
from . import views


urlpatterns = [
    path('my-cart/', views.CartAPIView.as_view({'read':  'detail'})),
]