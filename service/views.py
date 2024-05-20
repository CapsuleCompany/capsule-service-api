from rest_framework import viewsets
from rest_framework.response import Response
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from service.serializer import UserSerializer, CompanySerializer, LocationSerializer, ServiceSerializer, ServiceDetailSerializer, OrderSerializer, ScheduleSerializer, DetailSerializer
from service.models import User, Company, Location, Service, ServiceDetail, Order, Schedule, Detail
from rest_framework.decorators import action


class ProviderList(viewsets.GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.queryset
        service = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(service)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def get_services(self, request, pk=None):
        queryset = self.queryset.get(pk=pk).service_set.all()
        serializer = ServiceSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def get_service_details(self, request, pk=None, service_id=None):
        queryset = ServiceDetail.objects.filter(provider=service_id)
        serializer = ServiceDetailSerializer(queryset, many=True)
        return Response(serializer.data)



# class ServiceViewSet(viewsets.ModelViewSet):
#     """
#     A simple ViewSet for listing or retrieving services.
#     """
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
#
#     def list(self, request):
#         queryset = self.queryset
#         serializer = self.serializer_class(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = self.queryset
#         service = get_object_or_404(queryset, pk=pk)
#         serializer = self.serializer_class(service)
#         return Response(serializer.data)
#
#     @action(detail=True, methods=['get'])
#     def details(self, request, pk=None):
#         service = Detail.objects.all()
#         serializer = DetailSerializer(service, many=True)
#         return Response(serializer.data)
#













# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
#
#
# class LocationViewSet(viewsets.ModelViewSet):
#     queryset = Location.objects.all()
#     serializer_class = LocationSerializer
#
#
# class ServiceDetailViewSet(viewsets.ModelViewSet):
#     queryset = ServiceDetail.objects.all()
#     serializer_class = ServiceDetailSerializer
#
#
#
# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
#
# class ScheduleViewSet(viewsets.ModelViewSet):
#     queryset = Schedule.objects.all()
#     serializer_class = ScheduleSerializer
