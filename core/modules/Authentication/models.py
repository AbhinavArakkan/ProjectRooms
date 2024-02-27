from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class BoardMember(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name + "'s Board Member Details"

class NFCCard(models.Model):
    card_number = models.CharField(max_length=50, unique=True)
    card_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_used_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.card_name


class User(AbstractUser):
    ROLES = [
        ('Super Admin', 'Super Admin'),
        ('Admin', 'Admin'),
        ('Boardroom Director', 'Boardroom Director'),
        ('Boardroom Member', 'Boardroom Member'),
    ]

    name = models.CharField(max_length=100)
    nfc_card = models.ForeignKey(NFCCard, on_delete=models.SET_NULL, null=True)
    role = models.CharField(max_length=50, choices=ROLES)
    details = models.ForeignKey(BoardMember, on_delete=models.SET_NULL, null=True, blank=True, related_name='users_details')

    # Provide unique related names for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='authentication_user_groups',
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='authentication_user_permissions',
        blank=True,
    )

    def __str__(self):
        return self.username
    
    

class AuthenticationToken(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Token for {self.user.username}"

