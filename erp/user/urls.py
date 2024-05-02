from django.urls import path
from .views import RegisterUser, LoginUser, UpdateUserProfile, DeleteUser, LogoutUser

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register_user'),
    path('login/', LoginUser.as_view(), name='login_user'),
    path('update-profile/', UpdateUserProfile.as_view(), name='update_user_profile'),
    path('delete/', DeleteUser.as_view(), name='delete_user'),
    path('logout/', LogoutUser.as_view(), name='logout_user'),
]
