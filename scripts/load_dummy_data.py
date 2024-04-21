import random
from django.utils import timezone
from service.models import User, Customer, Location, Service, ServiceDetail, Order, Schedule


def run():
    # Create dummy users
    admin = User.objects.create(username='admin', email='admin@example.com', role='admin')
    contractor = User.objects.create(username='contractor', email='contractor@example.com', role='contractor')
    customer = User.objects.create(username='customer', email='customer@example.com', role='customer')

    # Create dummy customers
    customer1 = Customer.objects.create(name='John Doe', email='john@example.com', phone='1234567890')
    customer2 = Customer.objects.create(name='Jane Smith', email='jane@example.com', phone='9876543210')

    # Create dummy locations
    location1 = Location.objects.create(latitude=random.uniform(-90, 90), longitude=random.uniform(-180, 180))
    location2 = Location.objects.create(latitude=random.uniform(-90, 90), longitude=random.uniform(-180, 180))

    # Create dummy services
    service1 = Service.objects.create(name='Service 1', description='Description 1', price=50.0, category='Category 1', location=location1)
    service2 = Service.objects.create(name='Service 2', description='Description 2', price=75.0, category='Category 2', location=location2)

    # Create dummy service details
    service_detail1 = ServiceDetail.objects.create(name='Service Detail 1', description='Detail 1', price=25.0, service=service1)
    service_detail2 = ServiceDetail.objects.create(name='Service Detail 2', description='Detail 2', price=35.0, service=service2)

    # Create dummy orders
    order1 = Order.objects.create(customer=customer1, service=service1, meta='Meta 1')
    order2 = Order.objects.create(customer=customer2, service=service2, meta='Meta 2')

    # Create dummy schedules
    schedule1 = Schedule.objects.create(vendor_id=123456, service=service1, time=timezone.now())
    schedule2 = Schedule.objects.create(vendor_id=789012, service=service2, time=timezone.now())

if __name__ == "__main__":
    create_dummy_data()
