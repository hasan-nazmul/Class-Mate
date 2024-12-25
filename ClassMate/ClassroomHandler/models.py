from django.db import models
from UserHandler.models import CustomUser
import uuid

# Create your models here.
class Classroom(models.Model):
    class_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='teaching')
    class_name = models.CharField(max_length=100, default='Your Class')
    subject = models.CharField(max_length=100, blank=True)
    section = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cover_image = models.ImageField(upload_to='classroom_covers/')

    def __str__(self):
        return self.class_name
    
    class Meta: 
        ordering = ['-created_at'] 
        verbose_name = 'Classroom' 
        verbose_name_plural = 'Classrooms' 
        db_table = 'classroom_table' 

class Teaching(models.Model):
    teaching_class = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='teaching')
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='teacher')

    class Meta:
        unique_together = ['teaching_class', 'teacher']
        ordering = ['-teaching_class__created_at']