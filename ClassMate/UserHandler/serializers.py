from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'user_id',
            'username',
            'profile_image',
            'email'
        ]
        read_only_fields = ['user_id']
