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


    def to_dict(self):
        return {
            'user_id': str(self.user_id),
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'full_name': (str(self.first_name) + ' ' + str(self.last_name)) if self.last_name else str(self.first_name),
            'date_joined': self.date_joined.isoformat(),
            'last_login': self.last_login.isoformat() if self.last_login else None
        }
    
    def to_json(self):
        return json.dumps(self.to_dict())

    class Meta:
        db_table = 'CustomUserDB'
        ordering = ['date_joined']
        verbose_name = 'Classroom User'
        verbose_name_plural = 'Classroom Users'
        

    def __str__(self):
        return self.username
