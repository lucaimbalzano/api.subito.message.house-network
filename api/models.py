

import datetime
from email.policy import default
from enum import unique
import random
from django.db import models
from django.utils.translation import gettext_lazy as _
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
    energyClass = models.CharField(max_length=50)
    energyHeating = models.CharField(max_length=50)
    urlUserProfile = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)
    number = models.CharField(max_length=20)
    vetrina = models.BooleanField(default=False)
    advertising = models.CharField(max_length=100)
    location = models.CharField(max_length=150, default='NOT SPECIFIED')
    def __str__(self):
        return self.name


class Messages(models.Model):
    messageName = models.CharField(max_length = 100)
    dateAdded = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=5000)
    numberSent = models.ForeignKey(House, on_delete = models.CASCADE)

    def __str__(self):
        return self.messageName


class TrackProcess(models.Model):
    # default_idProc = 'ID::'+ str(datetime.datetime.now()).split(' ')[0]+'-'+str(random.randrange(999, 999999))
    identifierProcess = models.AutoField(primary_key=True)
    numPage = models.IntegerField(default=20)
    numCard = models.IntegerField(default=33)
    errorStack = models.CharField(max_length=10000, default='NO ERROR')
    dateStarted = models.DateTimeField(default=datetime.datetime.now)
    dateFinished = models.DateTimeField(default=None, blank=True, null=True)
    options = models.CharField(max_length=200, default=None, blank=True, null=True)
    seconds_execution = models.CharField(max_length=100, default=None, blank=True, null=True)
    minutes_execution = models.CharField(max_length=100, default=None, blank=True, null=True)
    def __str__(self):
        return self.options
    
class StateMachineProcess(models.Model):
    # class StatesType(models.TextChoices):
    #    ACTIVE = 'ACTIVE', _('ACTIVE')
    #    PAUSE = 'PAUSE', _('PAUSE')
    #    STOP = 'STOP', _('STOP')
    # state = models.CharField(choices=StatesType.choices,default=StatesType.STOP, max_length=50)
    id_state_machine = models.AutoField(primary_key=True)
    state = models.CharField(unique=True, max_length=10)
    processId = models.OneToOneField(TrackProcess, on_delete = models.CASCADE, unique=True)
    def __str__(self):
        return self.state




    