from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from .models import CustomUser  # Ensure you import CustomUser instead of User
from .serializers import CustomUserSerializer, CustomLoginSerializer


class CustomUserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]


class CustomLoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = CustomLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({"detail": "Successfully logged in"}, status=status.HTTP_200_OK)


# Example viewset that was causing the issue
class ProfileViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()  # Use CustomUser instead of User
    serializer_class = CustomUserSerializer
