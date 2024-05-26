from django.contrib import admin
from payment.models import Order, Payment, Customer


admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Customer)
