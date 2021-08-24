from django.db import models
from django.urls import reverse

# Create your models here.


class ContactRequest(models.Model):
    name = models.CharField(max_length=30, help_text="Your preferred name please")
    title = models.CharField(max_length=10, help_text="Examples: Mr, Ms, Mrs")
    subject = models.CharField(max_length=50, help_text="Try your best to summarize the topic of this message")
    comments = models.TextField(blank=True, null=True, help_text="The rest of your message. Try to be concise")
    email = models.EmailField()
    # the below two field will only be editable for admin
    resolved = models.BooleanField(default=False)
    commentFromAdmin = models.CharField(max_length=100, blank=True)

    def get_absolute_url(self):
        return reverse("contact:contact-home")
