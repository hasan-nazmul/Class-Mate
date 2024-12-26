from django.contrib import admin
from .models import *  # Import your Classroom model

class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('class_id', 'teacher', 'class_name', 'subject', 'created_at')  # Fields to display in admin list view

class EnrollmentsAdmin(admin.ModelAdmin):
    list_display = ('enrolled_class', 'student', 'enrolled_name', 'enrolled_id', 'joined_at')  # Fields to display in admin list view

admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Teaching)
admin.site.register(Enrollments, EnrollmentsAdmin)