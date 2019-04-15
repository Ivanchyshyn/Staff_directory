from django.contrib import admin
from .models import Boss, Employee, UserProfile

admin.site.register(Boss)
admin.site.register(Employee)
admin.site.register(UserProfile)