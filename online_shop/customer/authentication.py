from urllib.parse import non_hierarchical
from rest_framework.authentication import BaseAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token

class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', None)
        if token is None:
            return None
        
        try:
            token = Token.objects.get(key = token)
            print(token.user)
            return (token.user, None)
        except Exception:
            return None