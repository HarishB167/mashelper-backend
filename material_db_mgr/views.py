from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Material, MaterialLineItem, Unit
from .serializers import MaterialLineItemSerializer, MaterialSerializer, UnitSerializer

# Create your views here.
def hompage(request):
    return HttpResponse("Working")

class MaterialLineItemViewSet(ModelViewSet):
    queryset = MaterialLineItem.objects.all()
    serializer_class = MaterialLineItemSerializer

class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = []

class UnitViewSet(ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = []





