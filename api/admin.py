from django.contrib import admin
from .models import House, Messages, TimeManager, TrackProcess, MachineProcess


# Register your models here.
admin.site.register(House)
admin.site.register(Messages)
admin.site.register(TrackProcess)
admin.site.register(MachineProcess)
admin.site.register(TimeManager)

