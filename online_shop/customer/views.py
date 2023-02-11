from django.shortcuts import render
from rest_framework.authentication import(SessionAuthentication, BasicAuthentication, TokenAuthentication)
from rest_framework import generics, mixins, viewsets, views
from .serializers import CustomerSerializer, ProfileSerializer, LoginSerializer
from location.serializers import AddressSerializer
from .authentication import TokenAuthentication
from django.contrib.auth.models import User
from . import models
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password

from django.db.models.signals import pre_save, post_save
# from .tasks import send_registration_mail

# Create your views here.


class CustomerSignUp(views.APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = models.Customer.objects.create(
                username = serializer.validated_data['username'],
                email = serializer.validated_data['email'],
                full_name = serializer.validated_data['full_name'],
                password = make_password(serializer.validated_data['password']),
                phone_number = serializer.validated_data['phone_number']
            )

        return Response(
            {
                'username': user.username,
                'email': user.email,
                'password': user.password,
                'phone_numebr': user.phone_number,
                'full_name': user.full_name,
            }
        )

   

    #send_registration_mail(user.email)        ## Send registration mail
    
    

    
class CustomerLogIn(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = []

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        try:
            user = models.Customer.objects.get(
                Q(username=serializer.validated_data['username_or_email_or_phone']) |
                Q(email = serializer.validated_data['username_or_email_or_phone']) |
                Q(phone_number = serializer.validated_data['username_or_email_or_phone'])
            )
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {'token': token.key}
            )
        except Exception:
            return Response(
                data={
                    "username_or_email_or_phone": ["No account found with this email or username or number"]
                }
            )


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = models.Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, )

    def get_queryset(self, *args, **kwargs):
        
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(id = self.request.user.profile.id)
    
    