from django.db import models
from UserHandler.models import *
import uuid
import json

# Create your models here.
class Classroom(models.Model):
    class_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    instructor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='teaching')
    class_name = models.CharField(max_length=100, default='Your Class')
    subject = models.CharField(max_length=100, blank=True)
    section = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cover_image = models.ImageField(upload_to='classroom_covers/')
    students = models.ManyToManyField(CustomUser, related_name='enrolls')

    def to_dict(self):
        return {
            'class_id': str(self.class_id),
            'instructor': self.instructor.to_json(),
            'class_name': self.class_name,
            'subject': self.subject,
            'section': self.section,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'cover_image_url': self.cover_image.url if self.cover_image else None,
            'students': [str(student.user_id) for student in self.students.all()],
        }
    
    def to_json(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return self.class_name
    
    class Meta: 
        ordering = ['-created_at'] 
        verbose_name = 'Classroom' 
        verbose_name_plural = 'Classrooms' 
        db_table = 'classroom_table' 