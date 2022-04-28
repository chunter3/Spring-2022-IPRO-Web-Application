from django.contrib import admin
from Messaging_System.models import Chat, Message

# Register your models here.

admin.site.register(Message)
admin.site.register(Chat)