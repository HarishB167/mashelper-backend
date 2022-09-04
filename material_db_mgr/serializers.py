from rest_framework import serializers
from . import models

class MaterialLineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MaterialLineItem
        fields = ['id', 'date', 'location', 'remarks', 'quantity', 'material_name', 'unit']
