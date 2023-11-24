# myapp/models.py
from django.db import models

class Employees(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=300)
    salary = models.IntegerField()
    designation = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
