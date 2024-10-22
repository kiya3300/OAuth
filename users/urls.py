from django.urls import path
from .views import UserSignup, UserLogin, UserLogout, UserUpdateAPIView, PasswordResetRequest, PasswordResetConfirm, ProfileRetrieveUpdateDestroyAPIView, ProfileListCreateAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('signup/', UserSignup.as_view(), name='user-signup'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('logout/', UserLogout.as_view(), name='user-logout'),
    path('password-reset/', PasswordResetRequest.as_view(), name='password-reset-request'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password-reset-confirm'),
    path('api/users/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('profiles/', ProfileListCreateAPIView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileRetrieveUpdateDestroyAPIView.as_view(), name='profile-retrieve-update-destroy'),


]