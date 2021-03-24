from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('create/',views.RegisterView.as_view(),name='create'),
    path('profile/',views.CurrentUserView.as_view(),name='profile'),
    path('change-password/',views.ChangePasswordView.as_view(),name='change-password'),
    path('<int:pk>/',views.UserInfoAPIView.as_view(),name='info'),
    path('<int:pk>/avatar/',views.UserAvatarAPIView.as_view(),name='avatar'),
]