from django.shortcuts import render
from django.views.generic import ListView

from .models import Employee

class Home(ListView):
    model = Employee
    template_name = 'staff/index.html'
    context_object_name = 'staff'
    paginate_by = 100
    ordering = '-salary'


class Staff(Home):
    ordering = '-full_name'