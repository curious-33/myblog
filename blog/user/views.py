from django.contrib.auth import get_user_model
from rest_framework import generics, mixins, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from user.serializers import (ChangePasswordSerializer, RegisterSerializer,
                              UserAvatarSerializer, UserInfoSerializer)

from .permissions import IsOwnerOrReadOnly


class UsersApiRoot(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return Response({
            'Create user (Sign-Up)': reverse('user:create', request=request, format=format),
            'Create token for user': reverse('user:token_auth', request=request, format=format),
            "Current user's profile info": reverse('user:current-profile', request=request, format=format),
            "Current user's profile avatar": reverse('user:current-avatar', request=request, format=format),
            # "User info": reverse('user:user-info', request=request, format=format),
            # "Update user avatar": reverse('user:user-avatar', request=request, format=format),
            "Change password": reverse('user:change-password', request=request, format=format)
            })

class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class UserInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserInfoSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [IsOwnerOrReadOnly]

class UserAvatarAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserAvatarSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [IsOwnerOrReadOnly]

class CurrentUserAvatarAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserAvatarSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

class CurrentUserInfoView(generics.RetrieveUpdateAPIView):
    serializer_class = UserInfoSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # if using drf authtoken, create a new token 
        if hasattr(user, 'auth_token'):
            user.auth_token.delete()
        token, created = Token.objects.get_or_create(user=user)
        # return new token
        return Response({'token': token.key}, status=status.HTTP_200_OK)
