from django.shortcuts import render
from django.views.generic import ListView

from .models import Employee

class Home(ListView):
    model = Employee
    template_name = 'staff/index.html'
    context_object_name = 'staff'


class Staff(Home):
    template_name = 'staff/staff.html'