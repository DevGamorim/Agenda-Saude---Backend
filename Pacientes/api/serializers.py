from rest_framework import serializers
from Pacientes import models


class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pacientes
        fields = '__all__'