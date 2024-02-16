# contact/models.py
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    number = models.IntegerField()

    def __str__(self):
        return self.name


