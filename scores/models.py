from django.db import models
from django.urls import reverse
# Create your models here.

class Score(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    preview = models.ImageField(upload_to="scores/", blank=True)
    startDate = models.DateField(blank=True)
    publicUrl = models.URLField(blank=True, null=True)

    musescoreId = models.IntegerField(null=True, blank=True)
    designProcess = models.TextField(null=True, blank=True)
    def get_absolute_url(self):
        return reverse("scores:score-list", kwargs={}) 
