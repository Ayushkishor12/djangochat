from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100, null=True, blank=True)  # Optional location
    
    def __str__(self):
        return self.name


class Role(models.Model):  # Changed to PascalCase
    name = models.CharField(max_length=150, null=False)
    
    def __str__(self):
        return self.name


class Employee(models.Model):  # Changed to PascalCase
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=True, blank=True)  # Optional field
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)  # Changed to ForeignKey
    phone = models.CharField(max_length=15, null=True, blank=True)  # Changed to CharField
    hire_date = models.DateField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name or ''} ({self.phone or 'N/A'})"
