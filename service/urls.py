from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'services', views.ServiceViewSet)
router.register(r'providers', views.ProviderViewset)

# Custom URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Include default router URLs
    path('providers/<uuid:pk>/services', views.ProviderViewset.as_view({'get': 'get_services'}), name='get_services'),
    path('providers/<uuid:pk>/services/<uuid:service_id>', views.ProviderViewset.as_view({'get': 'get_service_details'}), name='get_services'),
    path('providers/<uuid:pk>/services/<uuid:service_id>/details/<uuid:details_id>', views.ProviderViewset.as_view({'get': 'get_details'}), name='get_services'),


    # path('services/<uuid:pk>/', views.ServiceViewSet.as_view({'get': 'retrieve'}), name='get_service'),
    # path('services/<uuid:pk>/service_detail', views.ServiceViewSet.as_view({'get': 'get_service_details'}), name='get_service_details_list'),
    # path('services/<uuid:pk>/service_detail/<uuid:detail_id>', views.ServiceViewSet.as_view({'get': 'get_service_details_list'}), name='service-detail'),
    # path('services/<uuid:pk>/provider', views.ServiceViewSet.as_view({'get': 'get_provider'}), name='service-detail'),
]
