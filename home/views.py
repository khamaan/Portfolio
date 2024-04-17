from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from .models import Contact
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # Validate email
        try:
            validate_email(email)
        except ValidationError:
            return render(request, "index.html", {'error': 'Invalid email'})

        # Validate subject
        if not subject:
            return render(request, "index.html", {'error': 'Subject is required'})

        # Check if user has already sent a message from the same IP address
        ip_address = request.META.get('REMOTE_ADDR')
        if Contact.objects.filter(ip_address=ip_address).count() >= 2:
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
