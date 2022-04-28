from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chat(models.Model):  
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')  
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')  
    has_unread = models.BooleanField(default=False)

class Message(models.Model):  
    chat = models.ForeignKey('Chat', related_name='+', on_delete=models.CASCADE, blank=True, null=True)  
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')  
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')  
    body = models.CharField(max_length=1000)  
    date = models.DateTimeField(auto_now_add=True)  
    is_read = models.BooleanField(default=False)