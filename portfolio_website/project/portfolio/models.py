from django.db import models
from datetime import datetime

# Create your models here.


class Projects(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to="images/")
    description = models.TextField(blank=True)
    technology = models.CharField(max_length=30)
    date_pub = models.DateTimeField(default=datetime.now, blank=True)
