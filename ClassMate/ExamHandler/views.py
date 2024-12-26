from django.shortcuts import render

# Create your views here.
def examroom(req, class_id):
    return render(req, 'examroom.html', context={'class_id': class_id})