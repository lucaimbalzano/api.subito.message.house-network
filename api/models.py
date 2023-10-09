

import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models import JSONField
from pytz import timezone as pytz_timezone
from email.policy import default
from enum import unique
import random


class House(models.Model):
    idHouse = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=150, default='NOT SPECIFIED')
    number = models.CharField(max_length=20)
    price = models.CharField(max_length=500)
    space = models.CharField(max_length=20)
    rooms = models.CharField(max_length=20)
    bathrooms = models.CharField(max_length=20)
    floor = models.CharField(max_length=30)
    totFloor = models.CharField(max_length=30)
    description = models.CharField(max_length=5000)
    parking = models.CharField(max_length=200)
    contract = models.CharField(max_length=20)
    typology = models.CharField(max_length=50)
    energyClass = models.CharField(max_length=50)
    energyHeating = models.CharField(max_length=50)
    energyUnit = models.CharField(max_length=30)
    urlUserProfile = models.CharField(max_length=1000)
    nameUser = models.CharField(max_length=200)
    otherCharacteristics = models.CharField(max_length=80)
    condominiumExpenses = models.CharField(max_length=30)
    caution = models.CharField(max_length=30)
    statusApartment = models.CharField(max_length=30)
    url = models.CharField(max_length=1000)
    refDataAnnuncio = models.CharField(max_length=30)
    vetrina = models.BooleanField(default=False)
    advertising = models.CharField(max_length=100)
    dateAdded = models.DateField(default=timezone.now().date())
    dateTimeAdded = models.TimeField(default=datetime.datetime.now().astimezone(pytz_timezone('Europe/Rome')).time())
    
    def __str__(self):
        return f"{self.idHouse}"


class Messages(models.Model):
    messageId = models.AutoField(primary_key=True)
    dateSent = models.DateField(default=timezone.now().date())
    dateTimeSent = models.TimeField(default=datetime.datetime.now().astimezone(pytz_timezone('Europe/Rome')).time())
    message = models.CharField(max_length=5000)
    house = models.ManyToManyField(House)
    options = models.CharField(max_length=200)

    def __str__(self):
         return f"{self.messageId} - {self.dateSent} - {self.message}"


class TimeManager(models.Model):
    idTimeManager = models.AutoField(primary_key=True)
    workAgentState  = models.CharField(max_length=20)
    cycleAgent  = models.CharField(max_length=20)
    numberCycle = models.IntegerField()
    addedDate = models.DateField(default=timezone.now().date())
    addedDateTime = models.TimeField(default=datetime.datetime.now().astimezone(pytz_timezone('Europe/Rome')).time())
    updateDate = models.DateField(null=True, blank=True)
    updateDateTime = models.TimeField(null=True, blank=True)
   
    def __str__(self):
        return f"{self.idTimeManager} - {self.workAgentState}"

class MachineProcess(models.Model):
    class StatesType(models.TextChoices):
       ACTIVE = 'PLAY', _('ACTIVE')
       PAUSE = 'PAUSE', _('PAUSE')
       STOP = 'STOP', _('STOP')
    
    idStateMachine = models.AutoField(primary_key=True)
    state = models.CharField(choices=StatesType.choices,default=StatesType.STOP, max_length=50)
    startedDate = models.DateField(default=timezone.now().date())
    startedDateTime = models.TimeField(default=datetime.datetime.now().astimezone(pytz_timezone('Europe/Rome')).time())
    finishDate =  models.DateField(null=True, blank=True) 
    finishDateTIme = models.TimeField(null=True, blank=True)
    timeManager = models.OneToOneField(TimeManager, on_delete = models.CASCADE, unique=True)

    def __str__(self):
        return f"{self.idStateMachine} - {self.startedDate}:{self.startedDateTime} - {self.state}"

class TrackProcess(models.Model):
    identifierProcess = models.AutoField(primary_key=True)
    numPage = models.IntegerField(default=20)
    numCard = models.IntegerField(default=33)
    urlLastPage = models.CharField(max_length=250)
    urlLastCard = models.CharField(max_length=250)
    options = models.CharField(max_length=200, default=None, blank=True, null=True)
    errorStack = models.CharField(max_length=10000, default='NO ERROR')
    machine = models.OneToOneField(MachineProcess, on_delete = models.CASCADE, unique=True)

    def __str__(self):
        return f"{self.identifierProcess}"
    


class FlowInputScraperConfig(models.Model):
    id_flow_input_scraper_config = models.AutoField(primary_key=True)
    totNumPage = models.CharField(max_length=4)
    totNumCards = models.CharField(max_length=4)
    contract = models.CharField(max_length=10)
    url = models.CharField(max_length=300)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    refreshSearch = JSONField()
    message = models.BooleanField()
    messageWebSite = models.BooleanField()
    default = models.BooleanField()



