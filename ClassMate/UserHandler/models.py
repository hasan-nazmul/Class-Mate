# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    username = models.CharField(max_length=255, unique=True)

    user_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    # Setting the email field as unique
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
