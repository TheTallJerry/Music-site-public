from django.db import models

# Create your models here.

class ScoreProject(models.Model):
    brass = models.BooleanField(default=True)
    saxophone = models.BooleanField(default=True)
    woodwinds = models.BooleanField(default=True)
    auxpercussion = models.BooleanField(default=True)
    drumset = models.BooleanField(default=True)
    piano = models.BooleanField(default=True)

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    composer = models.CharField(max_length=100, blank=True)
