from django.contrib import admin

# Register your models here.
from .models import Pacientes

#Apps
admin.site.register(Pacientes)