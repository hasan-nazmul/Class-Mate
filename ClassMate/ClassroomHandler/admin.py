from django.contrib import admin
from .models import *  # Import your Classroom model

class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('class_id', 'instructor', 'class_name', 'subject', 'created_at')  # Fields to display in admin list view

admin.site.register(Classroom, ClassroomAdmin)

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('announcement_id', 'classroom_id')  # Fields to display in admin list view

admin.site.register(Announcement, AnnouncementAdmin)

