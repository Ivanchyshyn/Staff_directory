from django.urls import path
from .views import Home, Staff

app_name = 'staff'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('staff/', Staff.as_view(), name='staff')
]