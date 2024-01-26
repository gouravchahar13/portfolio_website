from django.shortcuts import render,HttpResponse
import mimetypes
from django.contrib import messages
from .models import data as orignal_data
import pandas

# Create your views here.

def home(request):
    if request.method=='POST':
        data=request.POST
        name=data.get('Name')
        email=data.get('email')
        subject=data.get('subject')
        message=data.get('message')
        formdata=orignal_data.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        formdata.save()
        messages.info(request,'Form submitted successfully,Thank you for reaching out..')
        return render(request,'index.html')
    return render(request,'index.html')
