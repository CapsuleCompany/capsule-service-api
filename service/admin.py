from django.contrib import admin
from service.models import Detail, Service, ServiceDetail, Company
# # Register your models here.

admin.site.register(Service)
admin.site.register(ServiceDetail)
admin.site.register(Detail)
admin.site.register(Company)
