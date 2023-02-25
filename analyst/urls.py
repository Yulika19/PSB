from django.urls import path, include
from .views import UserRegistrationView
from .views import UserLoginView
from .views import main_page
from .views import PasswordChangeView
urlpatterns = [
     path('/register', UserRegistrationView.as_view(), name='register'),
     path('/login', UserLoginView.as_view(), name='login'),
     path('', main_page, name='main'),
     path('/change_password', PasswordChangeView.as_view(), name='change_password'),
]
