from django.urls import path
# from .views import CustomAuthView
from django.urls import path, include


urlpatterns = [
    # path('api/token/', CustomAuthView.as_view(), name='token_obtain_pair'),
    path('accounts/', include('allauth.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]
