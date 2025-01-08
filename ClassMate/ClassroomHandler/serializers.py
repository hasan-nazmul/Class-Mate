from rest_framework import serializers
from .models import Classroom
from UserHandler.models import CustomUser

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = [
            'class_id',
            'instructor',
            'class_name',
            'subject',
            'section',
            'description',
            'created_at',
            'cover_image',
            'students'
        ]
