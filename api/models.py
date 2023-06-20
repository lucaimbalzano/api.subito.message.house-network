

import datetime
from email.policy import default
from enum import unique
import random
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class House(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=150, default='NOT SPECIFIED')
    number = models.CharField(max_length=20)
    price = models.CharField(max_length=500)
    space = models.CharField(max_length=20)
    rooms = models.CharField(max_length=20)
    bathrooms = models.CharField(max_length=20)
    floor = models.CharField(max_length=10)
    totFloor = models.CharField(max_length=10)
    description = models.CharField(max_length=5000)
    parking = models.CharField(max_length=200)
    contract = models.CharField(max_length=20)
    typology = models.CharField(max_length=50)
    energyClass = models.CharField(max_length=50)
    energyHeating = models.CharField(max_length=50)
    energyUnit = models.CharField(max_length=15)
    urlUserProfile = models.CharField(max_length=1000)
    nameUser = models.CharField(max_length=200)
    otherCharacteristics = models.CharField(max_length=80)
    condominiumExpenses = models.CharField(max_length=10)
    caution = models.CharField(max_length=5)
    statusApartment = models.CharField(max_length=30)
    url = models.CharField(max_length=1000)
    refDataAnnuncio = models.CharField(max_length=30)
    vetrina = models.BooleanField(default=False)
    advertising = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nameUser


class Messages(models.Model):
    messageName = models.CharField(max_length = 100)
    dateAdded = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=5000)
    numberSent = models.ForeignKey(House, on_delete = models.CASCADE)

    def __str__(self):
        return self.messageName


class TimeManager(models.Model):
    messageName = models.CharField(max_length = 100)
    dateAdded = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=5000)
    numberSent = models.ForeignKey(House, on_delete = models.CASCADE)

    def __str__(self):
        return self.messageName

class MachineProcess(models.Model):
    class StatesType(models.TextChoices):
       ACTIVE = 'PLAY', _('ACTIVE')
       PAUSE = 'PAUSE', _('PAUSE')
       STOP = 'STOP', _('STOP')
    
    idStateMachine = models.AutoField(primary_key=True)
    # state = models.CharField(max_length=10)
    state = models.CharField(choices=StatesType.choices,default=StatesType.STOP, max_length=50)
    startedDate = models.DateTimeField(default=datetime.datetime.now)
    startedDateTime = models.TimeField(default=datetime.datetime.now)
    finishDate = models.DateTimeField(default=datetime.datetime.now) 
    finishDateTIme = models.TimeField()
    def __str__(self):
        return self.state

class TrackProcess(models.Model):
    # default_idProc = 'ID::'+ str(datetime.datetime.now()).split(' ')[0]+'-'+str(random.randrange(999, 999999))
    identifierProcess = models.AutoField(primary_key=True)
    numPage = models.IntegerField(default=20)
    numCard = models.IntegerField(default=33)
    urlLastPage = models.IntegerField(max_length=200)
    urlLastCard = models.IntegerField(max_length=200)
    options = models.CharField(max_length=200, default=None, blank=True, null=True)
    errorStack = models.CharField(max_length=10000, default='NO ERROR')
    machine = models.OneToOneField(MachineProcess, on_delete = models.CASCADE, unique=True)

    def __str__(self):
        return self.options
    


class UrlTrackProcess(models.Model):
    id_url_track_process = models.AutoField(primary_key=True)
    url_page = models.CharField(max_length=300)
    url_card = models.CharField(max_length=300)
    dateStarted = models.DateTimeField(default=datetime.datetime.now)
    seconds_execution = models.CharField(max_length=100, default=None, blank=True, null=True)
    minutes_execution = models.CharField(max_length=100, default=None, blank=True, null=True)
    def __str__(self):
        return self.url_page
    