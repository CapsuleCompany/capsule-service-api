from django.contrib import admin
from user.models import CustomUser, Profile, Notification


admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Notification)
