from rest_framework import viewsets

from service.serializer import UserSerializer, CustomerSerializer, LocationSerializer, ServiceSerializer, ServiceDetailSerializer, OrderSerializer, ScheduleSerializer
from service.models import User, Customer, Location, Service, ServiceDetail, Order, Schedule


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetailViewSet(viewsets.ModelViewSet):
    queryset = ServiceDetail.objects.all()
    serializer_class = ServiceDetailSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
