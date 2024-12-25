from django.contrib import admin
from .models import *  # Import your Classroom model

class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('class_id', 'teacher', 'class_name', 'subject', 'created_at')  # Fields to display in admin list view

admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Teaching)