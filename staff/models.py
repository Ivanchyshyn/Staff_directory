from django.db import models
from django.contrib.auth.models import User


class Boss(models.Model):
    full_name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Bosses'

    def __str__(self):
        return self.full_name


class Employee(models.Model):
    boss = models.ForeignKey(Boss, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=128)
    job = models.CharField(max_length=128)
    start_working_date = models.DateField()
    salary = models.DecimalField(max_digits=100, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Staff'

    def __str__(self):
        return self.full_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="profile_images", blank=True)

    def __str__(self):
        return self.user.username
