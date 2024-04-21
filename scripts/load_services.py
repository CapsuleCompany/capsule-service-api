import random

from service.models import User, Company, Location, Service, ServiceDetail, Detail, Category
from scripts.helper.services import services
from scripts.helper.locations import locations
from scripts.helper.users import general, admins, contractors


def create_or_get_user(user_data):
    email = user_data['email']
    user, created = User.objects.get_or_create(email=email, defaults=user_data)
    if not created:
        # Update existing user data if necessary
        for key, value in user_data.items():
            setattr(user, key, value)
        user.save()
    return user


def run():
    # Create dummy users
    for user_data in general:
        create_or_get_user(user_data)
    for user_data in admins:
        create_or_get_user(user_data)
    for user_data in contractors:
        create_or_get_user(user_data)

    # Create dummy services and details
    for service in services:
        # Check if the service already exists
        existing_service = Service.objects.filter(name=service['name']).first()
        if existing_service:
            print(f"Service '{service['name']}' already exists. Skipping creation.")
            continue

        location_data = random.choice(locations)
        location = Location.objects.create(
            latitude=location_data['latitude'],
            longitude=location_data['longitude']
        )

        user = User.objects.get(email=random.choice(contractors)['email'])
        company, _ = Company.objects.get_or_create(
            name=service['company_name'],
            defaults={
                'description': service['company_description'],
                'image': service['image'],
                'owner': user,
                'location': location
            }
        )

        category, _ = Category.objects.get_or_create(name=service['category'])

        # Create the service
        service_obj, _ = Service.objects.get_or_create(
            name=service['name'],
            defaults={
                'description': service['description'],
                'price': service['price'],
                'category': category,
                'location': location,
                'company': company,
                'image': service['image']
            }
        )

        # Create service details if the service is newly created
        if service_obj:
            for detail in service['details']:
                ServiceDetail.objects.create(provider=service_obj, **detail)

if __name__ == "__main__":
    run()
