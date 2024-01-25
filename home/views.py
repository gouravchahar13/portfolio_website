from django.shortcuts import render,HttpResponse
import mimetypes

# Create your views here.

def home(request):
    if request.method=='POST':
        data=request.POST
        name=data.get('Name')
        email=data.get('email')
        subject=data.get('subject')
        message=data.get('message')
        print(name,message,subject,email)
        return render(request,'index.html')
    return render(request,'index.html')

# def download_file(request):
#     # fill these variables with real values
#     fl_path = 'C:\Users\GOURAV CHAHAR\Desktop\gourav chahar\projects\django-projects\profile_website\servingcertificate.pdf'
#     filename = 'servingcertificate.pdf'

#     fl = open(fl_path, 'r')
#     mime_type, _ = mimetypes.guess_type(fl_path)
#     response = HttpResponse(fl, content_type=mime_type)
#     response['Content-Disposition'] = "attachment; filename=%s" % filename
#     return response
