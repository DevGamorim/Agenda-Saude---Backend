from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from Pacientes.api import serializers
from Pacientes import models


class PacientesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    serializer_class = serializers.PacientesSerializer
    queryset = models.Pacientes.objects.all()