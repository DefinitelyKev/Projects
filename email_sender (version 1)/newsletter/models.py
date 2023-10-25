from django.db import models
from datetime import datetime


# Create your models here.
class EmailSubmit(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    subject = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.title
