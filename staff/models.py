from django.db import models


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
