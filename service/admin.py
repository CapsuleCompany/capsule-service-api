from django.contrib import admin
from service.models import Detail, Service, ServiceDetail, Business, Category, Subcategory

admin.site.register(Service)
admin.site.register(ServiceDetail)
admin.site.register(Detail)
admin.site.register(Business)
admin.site.register(Category)
admin.site.register(Subcategory)
