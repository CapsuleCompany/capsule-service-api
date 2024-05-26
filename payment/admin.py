from django.contrib import admin
from payment.models import Order, Payment, OrderType, Customer


admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(OrderType)
admin.site.register(Customer)
