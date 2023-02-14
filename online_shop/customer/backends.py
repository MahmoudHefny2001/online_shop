from django.contrib.auth.models import User
from rest_framework import authentication, exceptions


class MultiUserName(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            header = request.META.get('HTTP_AUTHORIAZATION')
            if not username:
                return None
        except:
            return None 
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)
