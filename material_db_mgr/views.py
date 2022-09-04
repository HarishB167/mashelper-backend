from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Material, MaterialLineItem, Unit
from .serializers import ListMaterialLineItemSerializer, MaterialLineItemSerializer, MaterialSerializer, UnitSerializer


class MaterialLineItemViewSet(ModelViewSet):
    queryset = MaterialLineItem.objects.select_related('material_name', 'unit').all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListMaterialLineItemSerializer
        return MaterialLineItemSerializer

class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = []

class UnitViewSet(ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = []





