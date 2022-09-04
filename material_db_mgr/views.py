from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import MaterialLineItem
from .serializers import MaterialLineItemSerializer

# Create your views here.
def hompage(request):
    return HttpResponse("Working")

class MaterialLineItemViewSet(ModelViewSet):
    queryset = MaterialLineItem.objects.all()
    serializer_class = MaterialLineItemSerializer

    