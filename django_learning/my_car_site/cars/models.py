from django.db import models


# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=30)
    year = models.IntegerField()

    def __str__(self):
        return f"Car is Model: {self.brand}, Year: {self.year}"
