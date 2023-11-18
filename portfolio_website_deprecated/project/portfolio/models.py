from django.db import models
from datetime import datetime

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to="images/", default=None)
    description = models.TextField(blank=True)
    technology = models.CharField(max_length=30)
    date_pub = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
