from django.contrib.auth import login, logout
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import redirect
from authentication.models import User
from authentication.permissions import IsAdminOrSelf
from authentication.serializers import UserSerializer, LoginSerializer, ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Представление для работы с пользователем"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrSelf]

    def perform_create(self, serializer):
        user = serializer.save()
        password = serializer.validated_data['password']
        user.set_password(password)
        user.save()


class LoginView(generics.GenericAPIView):
    """Представление для логина пользователя"""
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        return Response({'detail': 'Успешный вход в систему'})


class ProfileView(generics.RetrieveAPIView):
    """Представление для просмотра профиля"""
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class LogoutView(generics.GenericAPIView):
    """Представление для выхода пользователя"""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return redirect('login')

    def get(self, request):
        logout(request)
        return redirect('login')

    def get_serializer_class(self):
        return None