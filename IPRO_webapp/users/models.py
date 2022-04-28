from django.db import models
from catalogue.models import Textbook

class WishList(models.Model):

    username = models.CharField(max_length=50)
    textbooks = models.ManyToManyField(Textbook, related_name="wishlists")

    def __str__(self):
        return self.username

class Fraud(models.Model):

    username = models.CharField(max_length=50)
    report = models.CharField(max_length=100)
    

    def __str__(self):
        return self.username
