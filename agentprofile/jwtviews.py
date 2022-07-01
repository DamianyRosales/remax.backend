from rest_framework import generics, status
from rest_framework_simplejwt.authentication import AUTH_HEADER_TYPES
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.settings import api_settings

from django.utils.module_loading import import_string
from django.http import JsonResponse

from agentprofile import serializers, models

class TokenViewBase(generics.GenericAPIView):
    permission_classes = ()
    authentication_classes = ()

    serializer_class = None
    _serializer_class = ""

    www_authenticate_realm = "api"

    def get_serializer_class(self):
        """
        If serializer_class is set, use it directly. Otherwise get the class from settings.
        """

        if self.serializer_class:
            return self.serializer_class
        try:
            return import_string(self._serializer_class)
        except ImportError:
            msg = "Could not import serializer '%s'" % self._serializer_class
            raise ImportError(msg)

    def get_authenticate_header(self, request):
        return '{} realm="{}"'.format(
            AUTH_HEADER_TYPES[0],
            self.www_authenticate_realm,
        )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        email = request.data.get('email')
        uemail = 'email'
        for i in models.AgentProfile.objects.all():
            if i.email == email:
                uemail = i.email
                ufull_name = i.fname + i.lname
                ufname = i.fname
                ulname = i.lname


        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
         
        return JsonResponse(data={'data':serializer.validated_data, 'email':uemail, 'fullname':ufull_name, 'fname':ufname, 'lname':ulname}, status=status.HTTP_200_OK)

class TokenObtainPairView(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """

    _serializer_class = api_settings.TOKEN_OBTAIN_SERIALIZER

class TokenRefreshView(TokenViewBase):
    """
    Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.
    """

    _serializer_class = api_settings.TOKEN_REFRESH_SERIALIZER

class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.TokenObtainPairSerializer

