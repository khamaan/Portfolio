from django.shortcuts import render
from django.core.mail import send_mail
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
        subject = f'New contact form submission from {name}'
        sender_email = settings.EMAIL_HOST_USER  # Use the same email as in settings.py
        recipient_email = ['khamaan5@gmail.com']  # Your email where you want to receive messages
        email_body = f"Name: {name}\nEmail: {email}\nsubject: {subject}\n\nMessage:\n{message}"
        send_mail(subject, message, email_body, sender_email, recipient_email)
        contact.save()
    return render(request,"index.html")

def post(request):
    return render(request,"post.html")

def store(request):
    return render(request,"store.html")