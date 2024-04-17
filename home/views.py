import re
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from .models import Contact
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import datetime

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # Validate email format
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return render(request, "index.html", {'error': 'Invalid email format'})

        # Validate email existence
        try:
            validate_email(email)
        except ValidationError:
            return render(request, "index.html", {'error': 'Invalid email'})

        # Validate subject
        if not subject:
            return render(request, "index.html", {'error': 'Subject is required'})

        # Check if user has already sent a message from the same IP address
        ip_address = request.META.get('REMOTE_ADDR')
        today = datetime.date.today()
        messages_sent_today = Contact.objects.filter(ip_address=ip_address, created_at__date=today).count()
        if messages_sent_today >= 2:
            return render(request, "index.html", {'error': 'You have reached the maximum limit of messages'})

        contact = Contact.objects.create(name=name, email=email, subject=subject, message=message, ip_address=ip_address)
        contact.save()

        to_email = "khamaan5@gmail.com"  # Your email where you want to receive messages
        email_body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\n\nMessage:\n{message}"
        email_message = EmailMultiAlternatives(subject, email_body, settings.EMAIL_HOST_USER, [to_email])
        email_message.send()

    return render(request, "index.html")

def post(request):
    return render(request,"post.html")

def store(request):
    return render(request,"store.html")
