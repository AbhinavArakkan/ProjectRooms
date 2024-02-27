
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import AuthenticationService
from .serializers import LoginSerializer

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if 'password' in serializer.validated_data:
            user = AuthenticationService.authenticate_user(
                serializer.validated_data['username'],
                serializer.validated_data['password']
            )
        else:
            user = AuthenticationService.authenticate_user_by_card(
                serializer.validated_data['card_number']
            )

        token = AuthenticationService.generate_authentication_token(user)

        return Response({'username': user.username, 'token': token}, status=status.HTTP_200_OK)
