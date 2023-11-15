from django.db import models


# Create your models here.
class SubscribedUsers(models.Model):
    email = models.EmailField(max_length=254, blank=False)
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name
