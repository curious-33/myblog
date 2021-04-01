from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from user import views

app_name = 'user'

urlpatterns = [
    path("",views.UsersApiRoot.as_view(),name="root-endpoints"),
    path('create/',views.RegisterView.as_view(),name='create'),
    path('token-auth/', obtain_auth_token, name='token_auth'),
    path('profile/',views.CurrentUserInfoView.as_view(),name='current-profile'),
    path('avatar/',views.CurrentUserAvatarAPIView.as_view(),name='current-avatar'),
    path('change-password/',views.ChangePasswordView.as_view(),name='change-password'),
    path('<int:pk>/',views.UserInfoAPIView.as_view(),name='user-info'),
    path('<int:pk>/avatar/',views.UserAvatarAPIView.as_view(),name='user-avatar'),
]