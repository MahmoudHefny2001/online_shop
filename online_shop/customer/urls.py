from django.urls import include, path, re_path
from rest_framework.authtoken import views as rest_views
from rest_framework.routers import DefaultRouter

from . import views

route = DefaultRouter()

# route.register(r'signup', views.CustomerSignUp)
route.register(r'profile', views.ProfileViewSet)

urlpatterns = [
    path('', include(route.urls)),
    path('login/', views.CustomerLogIn.as_view()),
    path('signup/', views.CustomerSignUp.as_view()),
    # path('profile/<int:pk>/', views.ProfileCreateAPIView.as_view()),

    path('logout/', views.Logout.as_view()),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),

    # re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf'))
    
]
