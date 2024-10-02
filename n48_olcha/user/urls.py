from django.urls import path
from .views import UserLoginApiView, UserLogoutApiView, UserRegistrationApiView

urlpatterns = [
    path('register/', UserRegistrationApiView.as_view(), name='register'),
    path('login/', UserLoginApiView.as_view(), name='login'),
    path('logout/', UserLogoutApiView.as_view(), name='logout'),
]

