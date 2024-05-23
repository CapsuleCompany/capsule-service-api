from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from service import views

router = DefaultRouter()
router.register(r'services', views.ServiceViewSet)
router.register(r'provider', views.BusinessViewSet)

# Custom URL patterns
urlpatterns = [
    path('', include(router.urls)),
    # path('provider/<uuid:pk>/reviews', views.BusinessViewSet.as_view({'get': 'get_reviews'}), name='get_reviews'),
    # path('provider/<uuid:pk>/contact', views.BusinessViewSet.as_view({'get': 'get_contact'}), name='get_contact'),
    path('provider/<uuid:pk>/services', views.BusinessViewSet.as_view({'get': 'get_services'}), name='get_services'),
    path('services/<uuid:service_id>', views.BusinessViewSet.as_view({'get': 'get_service_details'}), name='get_services'),
    path('services/<uuid:service_id>/details/<uuid:details_id>', views.BusinessViewSet.as_view({'get': 'get_details'}), name='get_services'),

    path('api/schema', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),


    # path('services/<uuid:pk>/', views.ServiceViewSet.as_view({'get': 'retrieve'}), name='get_service'),
    # path('services/<uuid:pk>/service_detail', views.ServiceViewSet.as_view({'get': 'get_service_details'}), name='get_service_details_list'),
    # path('services/<uuid:pk>/service_detail/<uuid:detail_id>', views.ServiceViewSet.as_view({'get': 'get_service_details_list'}), name='service-detail'),
    # path('services/<uuid:pk>/provider', views.ServiceViewSet.as_view({'get': 'get_provider'}), name='service-detail'),
]
