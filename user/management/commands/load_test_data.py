import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from service.models import Profile, Business, Category, Subcategory, Location, Address, Service, ServiceDetail, Review, Schedule, Appointment, Payment, Notification

class Command(BaseCommand):
    help = 'Load test data into the database'

    def handle(self, *args, **kwargs):
        # Get the custom user model
        CustomUser = get_user_model()

        # Create Users
        user1 = CustomUser.objects.create_user(phone='123-456-7890', password='password123', first_name='John', last_name='Doe', email='john@example.com')
        user2 = CustomUser.objects.create_user(phone='098-765-4321', password='password123', first_name='Jane', last_name='Doe', email='jane@example.com')

        # Create Profiles
        profile1 = Profile.objects.create(user=user1, email='john@example.com', role='contractor')
        profile2 = Profile.objects.create(user=user2, email='jane@example.com', role='contractor')

        # Create Locations
        location1 = Location.objects.create(latitude=40.7128, longitude=-74.0060)
        location2 = Location.objects.create(latitude=34.0522, longitude=-118.2437)

        # Create Addresses
        address1 = Address.objects.create(address_1='123 Main St', city='New York', state='NY', zip_code='10001', country='USA', location=location1)
        address2 = Address.objects.create(address_1='456 Elm St', city='Los Angeles', state='CA', zip_code='90001', country='USA', location=location2)

        # Create Businesses
        business1 = Business.objects.create(name='UrbanChic Hair Studio', description='Top-notch hairstyling services', owner=user1)
        business1.location.add(location1)
        business2 = Business.objects.create(name='Glamour Nails', description='High-quality nail services', owner=user2)
        business2.location.add(location2)

        # Create Categories
        category1 = Category.objects.create(name='Hair', description='Hair related services')
        category2 = Category.objects.create(name='Nails', description='Nail related services')

        # Create Subcategories
        subcategory1 = Subcategory.objects.create(name='Haircut', category=category1)
        subcategory2 = Subcategory.objects.create(name='Hair Coloring', category=category1)
        subcategory3 = Subcategory.objects.create(name='Manicure', category=category2)
        subcategory4 = Subcategory.objects.create(name='Pedicure', category=category2)

        # Create Services
        service1 = Service.objects.create(name='Basic Haircut', description='A basic haircut service', price=30.0, category=category1, company=business1)
        service1.subcategories.add(subcategory1)
        service1.locations.add(location1)

        service2 = Service.objects.create(name='Hair Coloring', description='Full hair coloring service', price=80.0, category=category1, company=business1)
        service2.subcategories.add(subcategory2)
        service2.locations.add(location1)

        service3 = Service.objects.create(name='Basic Manicure', description='A basic manicure service', price=20.0, category=category2, company=business2)
        service3.subcategories.add(subcategory3)
        service3.locations.add(location2)

        service4 = Service.objects.create(name='Basic Pedicure', description='A basic pedicure service', price=25.0, category=category2, company=business2)
        service4.subcategories.add(subcategory4)
        service4.locations.add(location2)

        service5 = Service.objects.create(name='Haircut and Style', description='Haircut and styling package', price=50.0, category=category1, company=business1)
        service5.subcategories.add(subcategory1)
        service5.locations.add(location1)

        # Create Service Details
        ServiceDetail.objects.create(name='Standard Haircut', service=service1, price=30.0, duration_min=30, duration_max=45)
        ServiceDetail.objects.create(name='Full Color', service=service2, price=80.0, duration_min=90, duration_max=120)
        ServiceDetail.objects.create(name='Classic Manicure', service=service3, price=20.0, duration_min=30, duration_max=45)
        ServiceDetail.objects.create(name='Classic Pedicure', service=service4, price=25.0, duration_min=45, duration_max=60)
        ServiceDetail.objects.create(name='Haircut and Blow-dry', service=service5, price=50.0, duration_min=60, duration_max=75)

        # Create Reviews
        Review.objects.create(service=service1, user=user1, rating=5, comment='Excellent service!')
        Review.objects.create(service=service2, user=user2, rating=4, comment='Good service but a bit pricey.')

        # Create Schedules
        schedule1 = Schedule.objects.create(vendor=user1, service=service1, time='2024-06-01T10:00:00Z')
        schedule2 = Schedule.objects.create(vendor=user2, service=service3, time='2024-06-01T14:00:00Z')

        # Create Appointments
        appointment1 = Appointment.objects.create(customer=user2, service=service1, schedule=schedule1, appointment_time='2024-06-01T10:00:00Z', deposit_amount=10.0, status='confirmed')
        appointment2 = Appointment.objects.create(customer=user1, service=service3, schedule=schedule2, appointment_time='2024-06-01T14:00:00Z', deposit_amount=5.0, status='pending')

        # Create Payments
        Payment.objects.create(appointment=appointment1, amount=30.0, payment_method='credit card', status='completed')
        Payment.objects.create(appointment=appointment2, amount=20.0, payment_method='cash', status='pending')

        # Create Notifications
        Notification.objects.create(user=user1, message='Your appointment is confirmed for Basic Haircut.', is_read=False)
        Notification.objects.create(user=user2, message='Your appointment is pending for Basic Manicure.', is_read=False)

        self.stdout.write(self.style.SUCCESS('Successfully loaded test data'))
