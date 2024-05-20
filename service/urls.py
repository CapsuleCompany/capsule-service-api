from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# router.register(r'services', views.ServiceViewSet)
router.register(r'providers', views.ProviderList)


# Custom URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Include default router URLs
    path('providers/<uuid:pk>/', views.ProviderList.as_view({'get': 'retrieve'}), name='provider-list'),
    path('providers/<uuid:pk>/services/', views.ProviderList.as_view({'get': 'get_services'}), name='provider-list'),
    path('providers/<uuid:pk>/services/<uuid:service_id>/', views.ProviderList.as_view({'get': 'get_service_details'}), name='provider-list'),
    # path('services/<int:pk>/', views.ServiceViewSet.as_view({'get': 'retrieve'}), name='service-detail'),
    # path('services/<int:pk>/details', views.ServiceViewSet.as_view({'get': 'details'}), name='service-details'),
]
