from django.db import models

class Textbook(models.Model):
    booktitle = models.CharField('Title', max_length=50)
    author = models.CharField('Author', max_length=30)
    isbn = models.CharField('ISBN', max_length=13)
    price = models.DecimalField('Price', default=0, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.booktitle
