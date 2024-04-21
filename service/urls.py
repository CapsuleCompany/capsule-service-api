from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'services', views.ServiceViewSet)
router.register(r'service-details', views.ServiceDetailViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'schedules', views.ScheduleViewSet)

urlpatterns = router.urls
