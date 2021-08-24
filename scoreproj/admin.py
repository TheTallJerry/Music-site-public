from django.contrib import admin
from .models import ScoreProject
# Register your models here.

class ScoreProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Instrumentation", {"fields": ["brass", "saxophone", "woodwinds", "auxPercussion", "drumset", "piano"]}), 
        ("Title of the project", {"fields": ["title"]}), 
        ("Main composer (if any) of the music", {"fields": ["composer"]}),
        ("Description (if any) of the project", {"fields": ["description"]}),
    ]

admin.site.register(ScoreProject, ScoreProjectAdmin)