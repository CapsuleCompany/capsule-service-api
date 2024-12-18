from rest_framework import viewsets
from rest_framework.response import Response
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from service.serializer import (
    ProviderSerializer,
    LocationSerializer,
    ServiceSerializer,
    ServiceDetailSerializer,
    DetailSerializer,
    CategorySerializer,
)
from service.models import (
    Business,
    Location,
    Service,
    ServiceDetail,
    Detail,
    Category,
)
from rest_framework.decorators import action


class BusinessViewset(viewsets.GenericViewSet):
    queryset = Business.objects.all()
    serializer_class = ProviderSerializer

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        Business = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(Business)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def get_services(self, request, pk=None):
        Business = get_object_or_404(self.queryset, pk=pk)
        services = Business.offered_services.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def get_service_details(self, request, pk=None, service_id=None):
        query = Service.objects.get(pk=service_id)
        serializer = ServiceSerializer(query, many=False)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def get_details(self, request, pk=None, service_id=None, details_id=None):
        details = ServiceDetail.objects.get(pk=details_id)
        serializer = ServiceDetailSerializer(details, many=False)
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

    @action(detail=True, methods=["get"])
    def get_service_details(self, request, pk=None):
        queryset = self.queryset
        service = get_object_or_404(queryset, pk=pk)
        all_provider_services = service.options.all()
        serializer = ServiceDetailSerializer(all_provider_services, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def get_service_details_list(self, request, pk=None, detail_id=None):
        queryset = self.queryset
        service = get_object_or_404(queryset, pk=pk)
        service_detail = service.options.all()
        service_detail = get_object_or_404(service_detail, pk=detail_id)
        serializer = ServiceDetailSerializer(service_detail, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def get_provider(self, request, pk=None):
        queryset = self.queryset
        provider = get_object_or_404(queryset, pk=pk)
        serializer = ProviderSerializer(provider.Business)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def get_provider_services(self, request, pk=None):
        queryset = self.queryset
        provider = get_object_or_404(queryset, pk=pk)
        all_provider_services = provider.Business.offered_services.all()
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

    @action(detail=True, methods=["get"])
    def get_services_by_category(self, request, pk=None):
        pass


# class ProfileViewset(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


#
# class BusinessViewSet(viewsets.ModelViewSet):
#     queryset = Business.objects.all()
#     serializer_class = BusinessSerializer
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
