from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import NFCCard, User

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    password = serializers.CharField(style={'input_type': 'password'}, required=False)
    card_number = serializers.CharField(required=False)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        card_number = data.get('card_number')

        if not (username and password) and not card_number:
            raise serializers.ValidationError('Must include either "username" and "password" or "card_number".')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise serializers.ValidationError('User account is disabled.')
            else:
                raise serializers.ValidationError('Unable to login with provided credentials.')

        elif card_number:
            try:
                user = User.objects.get(nfc_card__card_number=card_number)
            except User.DoesNotExist:
                raise serializers.ValidationError('User not found for the provided NFC card number.')

            if not user.role == 'Super Admin':
                raise serializers.ValidationError('Only Super Admins are allowed to login via NFC card.')

            data['user'] = user

        return data
