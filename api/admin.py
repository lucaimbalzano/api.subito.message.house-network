from django.contrib import admin
from .models import House, Messages, TrackProcess, MachineProcess


# Register your models here.
admin.site.register(House)
admin.site.register(Messages)
admin.site.register(TrackProcess)
admin.site.register(MachineProcess)

