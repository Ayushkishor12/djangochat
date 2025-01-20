from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, null=False)

    
class role(models.Model):
    name=models.CharField(max_length=150, null=False)
    
    
class Employe(models.Model):
    first_name=models.CharField(max_length=100, null=False)
    last_name=models.CharField(max_length=100)
    dept=models.ForeignKey(Department, on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.IntegerField(default=0)
    phone=models.IntegerField(default=0)
    hire_date=models.DateField()