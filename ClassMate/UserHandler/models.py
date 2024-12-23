# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Setting the username field as the primary key
    username = models.CharField(max_length=255, unique=True, primary_key=True)

    # Setting the email field as unique
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
