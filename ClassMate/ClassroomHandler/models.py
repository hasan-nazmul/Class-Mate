from django.db import models
from UserHandler.models import CustomUser
import uuid

# Create your models here.
class Classroom(models.Model):
    class_id = models.UUIDField(uuid.uuid4, editable=False, primary_key=True)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='teaching')
    class_name = models.CharField(max_length=100, blank=True, default='Your Class')
    subject = models.CharField(max_length=100, blank=True)
    section = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cover_image = models.ImageField(upload_to='classroom_covers/')

