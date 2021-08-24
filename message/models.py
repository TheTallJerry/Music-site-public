from django.db import models

# Create your models here.

class Message(models.Model):
    subject = models.CharField(max_length=40, default="subject")
    content = models.TextField(blank=True, null=True)