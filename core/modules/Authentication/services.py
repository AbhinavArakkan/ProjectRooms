
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from .models import User, AuthenticationToken

class AuthenticationService:
    @staticmethod
    def authenticate_user(username, password):
        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError('Unable to login with provided credentials.')
        if not user.is_active:
            raise ValidationError('User account is disabled.')
        return user

    @staticmethod
    def authenticate_user_by_card(card_number):
        try:
            user = User.objects.get(nfc_card__card_number=card_number)
        except User.DoesNotExist:
            raise ValidationError('User not found for the provided NFC card number.')

        if not user.role == 'Super Admin':
            raise ValidationError('Only Super Admins are allowed to login via NFC card.')

        return user

    @staticmethod
    def generate_authentication_token(user):
        token_obj, created = AuthenticationToken.objects.get_or_create(user=user)

        if created:
            token = AuthenticationToken.generate_token(user)
            token_obj.token = token
            token_obj.save()
            print("New Authentication Token generated:", token)
        else:
            print("Existing Authentication Token retrieved:", token_obj.token)

        return token_obj.token
