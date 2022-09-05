from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Material, MaterialLineItem, Unit
from .serializers import ListMaterialLineItemSerializer, MaterialLineItemSerializer, MaterialSerializer, UnitSerializer


class MaterialLineItemViewSet(ModelViewSet):
    queryset = MaterialLineItem.objects.select_related('material_name', 'unit').all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListMaterialLineItemSerializer
        return MaterialLineItemSerializer


class AddListMaterialItemViewSet(ModelViewSet):
    queryset = MaterialLineItem.objects.all()
    serializer_class = MaterialLineItemSerializer

@api_view(['GET', 'POST'])
def materiallineitem_list(request):
    if request.method == 'GET':
        queryset = MaterialLineItem.objects.all()
        serializer = MaterialLineItemSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MaterialLineItemSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = []

class UnitViewSet(ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = []





