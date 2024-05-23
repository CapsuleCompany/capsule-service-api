from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import CustomUserCreateView, CustomLoginView, ProfileViewset

router = DefaultRouter()
router.register(r'profiles', ProfileViewset, basename='profile')

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
    path('', include('dj_rest_auth.urls')),  # for dj-rest-auth
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', CustomUserCreateView.as_view(), name='register'),
    path('signup/', include('dj_rest_auth.registration.urls')),
]
