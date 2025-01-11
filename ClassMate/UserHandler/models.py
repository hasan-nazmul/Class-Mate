# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import json

class CustomUser(AbstractUser):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    profile_image = models.ImageField(upload_to='user_profile_images/', blank=True, null=True)
    email = models.EmailField(unique=True)
    classroom_count = models.IntegerField(default=0)


    class Meta:
        db_table = 'CustomUserDB'
        ordering = ['date_joined']
        verbose_name = 'Classroom User'
        verbose_name_plural = 'Classroom Users'
        

    def __str__(self):
        return self.username
