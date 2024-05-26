from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
    SpectacularJSONAPIView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("service.urls")),
    path("api/", include("user.urls")),
    path("api/", include("payment.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path(
        "api/openapi/",
        SpectacularJSONAPIView.as_view(authentication_classes=[]),
        name="openapi",
    ),
]
