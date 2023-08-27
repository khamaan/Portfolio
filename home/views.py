from django.shortcuts import render
from .models import Contact

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact.objects.create(name=name,email=email,subject=subject,message=message)
        contact.save()
    return render(request,"index.html")

def post(request):
    return render(request,"post.html")

def store(request):
    return render(request,"store.html")