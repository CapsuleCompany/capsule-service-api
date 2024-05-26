from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"service", views.ServiceViewSet)
router.register(r"business", views.BusinessViewset)
router.register(r"category", views.CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),  # Include default router URLs
    path(
        "business/<uuid:pk>/services/",
        views.BusinessViewset.as_view({"get": "get_services"}),
        name="get_services",
    ),
]
