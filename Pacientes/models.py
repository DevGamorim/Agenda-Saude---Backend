from django.db import models
from uuid import uuid4
from django.conf import settings

# Create your models here.
class Pacientes(models.Model):
    id_paciente = models.UUIDField(primary_key=True, default= uuid4, editable=False)
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
	    return self.cpf
