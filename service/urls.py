from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from . import views

router = DefaultRouter()
router.register(r'service', views.ServiceViewSet)
router.register(r'business', views.BusinessViewset)
router.register(r'category', views.CategoryViewSet)
# router.register(r'profile', views.ProfileViewset)

# Custom URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Include default router URLs
    path('business/<uuid:pk>/services', views.BusinessViewset.as_view({'get': 'get_services'}), name='get_services'),
    # path('providers/<uuid:pk>/services/<uuid:service_id>', views.BusinessViewset.as_view({'get': 'get_service_details'}), name='get_services'),
    # path('providers/<uuid:pk>/services/<uuid:service_id>/details/<uuid:details_id>', views.BusinessViewset.as_view({'get': 'get_details'}), name='get_services'),

    path('api/schema', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),


    # path('services/<uuid:pk>/', views.ServiceViewSet.as_view({'get': 'retrieve'}), name='get_service'),
    # path('services/<uuid:pk>/service_detail', views.ServiceViewSet.as_view({'get': 'get_service_details'}), name='get_service_details_list'),
    # path('services/<uuid:pk>/service_detail/<uuid:detail_id>', views.ServiceViewSet.as_view({'get': 'get_service_details_list'}), name='service-detail'),
    # path('services/<uuid:pk>/provider', views.ServiceViewSet.as_view({'get': 'get_provider'}), name='service-detail'),
]
