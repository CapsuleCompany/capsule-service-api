from django.contrib import admin
from schedule.models import Schedule, Appointment, Event, Occurrence


admin.site.register(Schedule)
admin.site.register(Appointment)
admin.site.register(Event)
admin.site.register(Occurrence)
