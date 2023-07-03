from django.contrib import admin
from .models import House, Messages, TimeManager, TrackProcess, MachineProcess, FlowInputScraperConfig


# Register your models here.
admin.site.register(House)
admin.site.register(Messages)
admin.site.register(TrackProcess)
admin.site.register(MachineProcess)
admin.site.register(TimeManager)
admin.site.register(FlowInputScraperConfig)

