import random
import uuid
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from service.models import Profile, Business, Category, Subcategory, Location, Address, Service, ServiceDetail, Review, Schedule, Appointment, Payment, Notification

class Command(BaseCommand):
    help = 'Load test data into the database'

    def handle(self, *args, **kwargs):
        # Get the custom user model
        CustomUser = get_user_model()

        # Create Users
        user1, created = CustomUser.objects.get_or_create(email='john@example.com', defaults={'password': 'password123', 'first_name': 'John', 'last_name': 'Doe', 'phone': '123-456-7890'})
        user2, created = CustomUser.objects.get_or_create(email='jane@example.com', defaults={'password': 'password123', 'first_name': 'Jane', 'last_name': 'Doe', 'phone': '098-765-4321'})

        # Create Profiles
        profile1, created = Profile.objects.get_or_create(user=user1, defaults={'email': 'john@example.com', 'role': 'contractor'})
        profile2, created = Profile.objects.get_or_create(user=user2, defaults={'email': 'jane@example.com', 'role': 'contractor'})

        # Create Locations
        location1, created = Location.objects.get_or_create(latitude=40.7128, longitude=-74.0060)
        location2, created = Location.objects.get_or_create(latitude=34.0522, longitude=-118.2437)

        # Create Addresses
        address1, created = Address.objects.get_or_create(address_1='123 Main St', city='New York', state='NY', zip_code='10001', country='USA', location=location1)
        address2, created = Address.objects.get_or_create(address_1='456 Elm St', city='Los Angeles', state='CA', zip_code='90001', country='USA', location=location2)

        # Create Businesses
        business1, created = Business.objects.get_or_create(name='UrbanChic Hair Studio', defaults={'description': 'Top-notch hairstyling services', 'owner': user1})
        business1.location.add(location1)
        business2, created = Business.objects.get_or_create(name='Glamour Nails', defaults={'description': 'High-quality nail services', 'owner': user2})
        business2.location.add(location2)

        # Create Category
        beauty_category, created = Category.objects.get_or_create(name='Beauty', defaults={'description': 'Beauty related services'})

        # Create Subcategories
        subcategories_data = [
            {"id": "c6def26d-08ac-4b82-ae17-8fd9f2c62c9d", "name": "Hair"},
            {"id": "4123786c-fec5-4a9f-a3dc-b4237a8a830c", "name": "Nails"}
        ]

        subcategories = []
        for subcategory_data in subcategories_data:
            subcategory, created = Subcategory.objects.get_or_create(id=uuid.UUID(subcategory_data["id"]), defaults={"name": subcategory_data["name"], "category": beauty_category})
            subcategories.append(subcategory)

        # Create Services
        service1, created = Service.objects.get_or_create(name='Basic Haircut', defaults={'description': 'A basic haircut service', 'price': 30.0, 'category': beauty_category, 'company': business1})
        service1.subcategories.add(subcategories[0])
        service1.locations.add(location1)

        service2, created = Service.objects.get_or_create(name='Hair Coloring', defaults={'description': 'Full hair coloring service', 'price': 80.0, 'category': beauty_category, 'company': business1})
        service2.subcategories.add(subcategories[0])
        service2.locations.add(location1)

        service3, created = Service.objects.get_or_create(name='Basic Manicure', defaults={'description': 'A basic manicure service', 'price': 20.0, 'category': beauty_category, 'company': business2})
        service3.subcategories.add(subcategories[1])
        service3.locations.add(location2)

        service4, created = Service.objects.get_or_create(name='Basic Pedicure', defaults={'description': 'A basic pedicure service', 'price': 25.0, 'category': beauty_category, 'company': business2})
        service4.subcategories.add(subcategories[1])
        service4.locations.add(location2)

        service5, created = Service.objects.get_or_create(name='Haircut and Style', defaults={'description': 'Haircut and styling package', 'price': 50.0, 'category': beauty_category, 'company': business1})
        service5.subcategories.add(subcategories[0])
        service5.locations.add(location1)

        # Create Service Details
        ServiceDetail.objects.get_or_create(name='Standard Haircut', service=service1, defaults={'price': 30.0, 'duration_min': 30, 'duration_max': 45})
        ServiceDetail.objects.get_or_create(name='Full Color', service=service2, defaults={'price': 80.0, 'duration_min': 90, 'duration_max': 120})
        ServiceDetail.objects.get_or_create(name='Classic Manicure', service=service3, defaults={'price': 20.0, 'duration_min': 30, 'duration_max': 45})
        ServiceDetail.objects.get_or_create(name='Classic Pedicure', service=service4, defaults={'price': 25.0, 'duration_min': 45, 'duration_max': 60})
        ServiceDetail.objects.get_or_create(name='Haircut and Blow-dry', service=service5, defaults={'price': 50.0, 'duration_min': 60, 'duration_max': 75})

        # Create Reviews
        Review.objects.get_or_create(service=service1, user=user1, defaults={'rating': 5, 'comment': 'Excellent service!'})
        Review.objects.get_or_create(service=service2, user=user2, defaults={'rating': 4, 'comment': 'Good service but a bit pricey.'})

        # Create Schedules
        schedule1, created = Schedule.objects.get_or_create(vendor=user1, service=service1, defaults={'time': '2024-06-01T10:00:00Z'})
        schedule2, created = Schedule.objects.get_or_create(vendor=user2, service=service3, defaults={'time': '2024-06-01T14:00:00Z'})

        # Create Appointments
        appointment1, created = Appointment.objects.get_or_create(customer=user2, service=service1, schedule=schedule1, defaults={'appointment_time': '2024-06-01T10:00:00Z', 'deposit_amount': 10.0, 'status': 'confirmed'})
        appointment2, created = Appointment.objects.get_or_create(customer=user1, service=service3, schedule=schedule2, defaults={'appointment_time': '2024-06-01T14:00:00Z', 'deposit_amount': 5.0, 'status': 'pending'})

        # Create Payments
        Payment.objects.get_or_create(appointment=appointment1, defaults={'amount': 30.0, 'payment_method': 'credit card', 'status': 'completed'})
        Payment.objects.get_or_create(appointment=appointment2, defaults={'amount': 20.0, 'payment_method': 'cash', 'status': 'pending'})

        # Create Notifications
        Notification.objects.get_or_create(user=user1, defaults={'message': 'Your appointment is confirmed for Basic Haircut.', 'is_read': False})
        Notification.objects.get_or_create(user=user2, defaults={'message': 'Your appointment is pending for Basic Manicure.', 'is_read': False})

        self.stdout.write(self.style.SUCCESS('Successfully loaded test data'))
