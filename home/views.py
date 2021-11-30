from django import contrib
from django.contrib import messages
from django.shortcuts import render

from .models import *

# Create your views here.

def home(request):
    
    if request.method == 'POST' and request.FILES == ['image']:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        department = request.POST.get('department')
        username = request.POST.get('user_name')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')
        image = request.FILES['image']
        print(first_name)
        if Student.objects.filter(email=email).exists():
            messages.success(request, 'Email already exists')
        else:
            Student.objects.create(first_name = first_name, last_name= last_name,
            department = department, username= username, email = email, contact_no = contact_no, image = image)
            messages.success(request, 'Student created Successfully')
    return render(request, 'registration.html')
