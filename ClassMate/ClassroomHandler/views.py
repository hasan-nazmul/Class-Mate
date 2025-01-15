from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from ClassroomHandler.serializers import *
from django.core.exceptions import ValidationError
from rest_framework.parsers import JSONParser
from django.contrib import messages
# # Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def classroom(req, class_id):
    current_classroom = cache.get(f'classroom:{class_id}')

    if not current_classroom:
        current_classroom = Classroom.objects.filter(class_id = class_id)[0]
        cache.set(f'classroom:{class_id}', current_classroom)

    if req.method == 'POST':
        image = req.FILES.get('cover_image')

        if image:
            current_classroom = Classroom.objects.filter(class_id = class_id)[0]
            current_classroom.cover_image = image
            current_classroom.save()
            cache.set(f'classroom:{class_id}', current_classroom)

        return redirect(f'/classroom/{class_id}')

    return render(req, 'classroom.html', context={'classroom': current_classroom})

