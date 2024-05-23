from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import CustomUserCreateView, CustomLoginView, ProfileViewset

router = DefaultRouter()
router.register(r'profiles', ProfileViewset, basename='profile')

urlpatterns = [
    path('auth/registration/', CustomUserCreateView.as_view(), name='register'),
    path('auth/login/', CustomLoginView.as_view(), name='login'),
    path('auth/', include('dj_rest_auth.urls')),  # for dj-rest-auth
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', include(router.urls)),  # Include the router URLs
]
