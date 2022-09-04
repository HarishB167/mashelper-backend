from rest_framework import serializers
from . import models

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Unit
        fields = ['id', 'unit']


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Material
        fields = ['id', 'name']

class MaterialLineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MaterialLineItem
        fields = ['id', 'date', 'location', 'remarks', 'quantity', 'material_name', 'unit']


class ListMaterialLineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MaterialLineItem
        fields = ['id', 'date', 'location', 'remarks', 'quantity', 'material_name', 'unit']
    
    material_name = MaterialSerializer()
    unit = UnitSerializer()
    