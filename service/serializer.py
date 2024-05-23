from rest_framework import serializers
from service.models import Business, Location, Service, ServiceDetail, Order, Schedule, Detail, Category


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        exclude = ['created_at', 'updated_at']


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        exclude = ['created_at', 'updated_at']


class ServiceDetailSerializer(serializers.ModelSerializer):
    user_inputs = DetailSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceDetail
        fields = ['id', 'name', 'description', 'price', 'image', 'user_inputs']


class ServiceSerializer(serializers.ModelSerializer):
    options = ServiceDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'price', 'image', 'category', 'options']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['created_at', 'updated_at']


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        exclude = ['created_at', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
        depth = 1


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        exclude = ['created_at', 'updated_at']
        depth = 2
