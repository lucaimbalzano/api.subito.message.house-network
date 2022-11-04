from email.policy import default
from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=500)
    space = models.CharField(max_length=20)
    rooms = models.CharField(max_length=20)
    floor = models.CharField(max_length=20)
    bathrooms = models.CharField(max_length=20)
    description = models.CharField(max_length=5000)
    title = models.CharField(max_length=100)
    parking = models.CharField(max_length=200)
    energyClass = models.CharField(max_length=20)
    energyHeating = models.CharField(max_length=20)
    urlUserProfile = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)
    number = models.CharField(unique=True,max_length=20)
    vetrina = models.BooleanField(default=False)
    advertising = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Messages(models.Model):
    messageName = models.CharField(max_length = 100)
    dateAdded = models.DateField(auto_now_add=True)
    message = models.CharField(max_length=5000)
    numberSent = models.ForeignKey(House, on_delete = models.CASCADE)

    def __str__(self):
        return self.messageName
    