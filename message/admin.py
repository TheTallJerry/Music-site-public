from django.contrib import admin
from .models import Message
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Subject of the message", {"fields": ["subject"]}), 
        ("Content of the message (if any)", {"fields": ["content"]})
    ]
admin.site.register(Message, MessageAdmin)