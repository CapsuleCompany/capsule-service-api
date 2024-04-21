from rest_framework import serializers
from service.models import User, Company, Location, Service, ServiceDetail, Order, Schedule


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ['created_at', 'updated_at']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        exclude = ['created_at', 'updated_at']


class ServiceSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Service
        exclude = ['created_at', 'updated_at']


class ServiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDetail
        exclude = ['created_at', 'updated_at']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['created_at', 'updated_at']


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        exclude = ['created_at', 'updated_at']
