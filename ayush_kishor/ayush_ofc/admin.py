from django.contrib import admin

# Register your models here.
from .models import Employe,role,Department

admin.site.register(Employe)
admin.site.register(role)
admin.site.register(Department)
