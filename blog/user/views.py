from django.contrib.auth import get_user_model
from rest_framework import generics, mixins, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from user.serializers import (ChangePasswordSerializer, RegisterSerializer,
                              UserAvatarSerializer, UserInfoSerializer)

from .permissions import IsOwnerOrReadOnly

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

class CurrentUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserInfoSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        serializer = UserInfoSerializer(request.user)
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
