from django.db import models

# Create your models here.


class EmployeeDetails(models.Model):
    employee_name = models.CharField(max_length=150)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    designation = models.CharField(max_length=100)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.email






    