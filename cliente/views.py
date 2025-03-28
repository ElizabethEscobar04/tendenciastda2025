from rest_framework import viewsets

from cliente.serializer import ClienteSerializer
from .models import Cliente

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()