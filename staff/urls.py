from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import HomeView, StaffView
from .views import register

app_name = 'staff'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='register/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('staff/', StaffView.as_view(), name='staff')
]