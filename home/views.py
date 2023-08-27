from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from .models import Contact
from django.conf import settings

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact.objects.create(name=name,email=email,subject=subject,message=message)
        contact.save()
        subject = f'New contact form submission from {name}'
        to_email = "khamaan5@gmail.com"  # Your email where you want to receive messages
        email_body = f"Name: {name}\nEmail: {email}\nsubject: {subject}\n\nMessage:\n{message}"
        email_message = EmailMultiAlternatives(subject, email_body, settings.EMAIL_HOST_USER, [to_email])
        email_message.send()
    return render(request,"index.html")

def post(request):
    return render(request,"post.html")

def store(request):
    return render(request,"store.html")