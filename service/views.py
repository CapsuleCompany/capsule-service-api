from rest_framework import viewsets
from rest_framework.response import Response
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from service.serializer import (UserSerializer, BusinessSerializer, LocationSerializer, ServiceSerializer,
                                ServiceDetailSerializer, ServiceReviewSerializer,
                                OrderSerializer, ScheduleSerializer, DetailSerializer,
                                CategorySerializer, ReviewSerializer)
from service.models import Profile, Business, Location, Service, ServiceDetail, Order, Schedule, Detail, Category, Review
from rest_framework.decorators import action


class BusinessViewSet(viewsets.GenericViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        company = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(company)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def get_services(self, request, pk=None):
        """Lists the services offered by a business"""

        company = get_object_or_404(self.queryset, pk=pk)
        services = company.offered_services.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def get_service_details(self, request, pk=None, service_id=None):
        """Gets details on the service offered"""

        query = Service.objects.get(pk=service_id)
        serializer = ServiceSerializer(query, many=False)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def get_details(self, request, pk=None, service_id=None, details_id=None):
        """Gets the options for service"""
        details = ServiceDetail.objects.get(pk=details_id)
        serializer = ServiceDetailSerializer(details, many=False)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def get_reviews(self, request, pk=None):
        """Get all the reviews for a customer ordered by service"""

        company = get_object_or_404(Business, pk=pk)
        services = company.offered_services.all()
        serializer = ServiceReviewSerializer(services, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def get_contact(self, request, pk=None):
        """Get contact info for a customer"""

        company = get_object_or_404(Business, pk=pk)
        owner = company.owner
        serializer = UserSerializer(owner, many=False)
        return Response(serializer.data)


class ServiceViewSet(viewsets.GenericViewSet):
    """
    A simple ViewSet for listing or retrieving services.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

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
    def get_service_details(self, request, pk=None):
        queryset = self.queryset
        service = get_object_or_404(queryset, pk=pk)
        all_provider_services = service.options.all()
        serializer = ServiceDetailSerializer(all_provider_services, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def get_service_details_list(self, request, pk=None, detail_id=None):
        queryset = self.queryset
        service = get_object_or_404(queryset, pk=pk)
        service_detail = service.options.all()
        service_detail = get_object_or_404(service_detail, pk=detail_id)
        serializer = ServiceDetailSerializer(service_detail, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def get_provider(self, request, pk=None):
        queryset = self.queryset
        provider = get_object_or_404(queryset, pk=pk)
        serializer = BusinessSerializer(provider.company)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def get_provider_services(self, request, pk=None):
        queryset = self.queryset
        provider = get_object_or_404(queryset, pk=pk)
        all_provider_services = provider.company.offered_services.all()
        serializer = ServiceSerializer(all_provider_services, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

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
    def get_services_by_category(self, request, pk=None):
        pass





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
