from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)  # Make the field nullable
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return self.name
