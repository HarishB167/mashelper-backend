import csv
from datetime import datetime
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Material, MaterialLineItem, Unit
from .serializers import ListMaterialLineItemSerializer, MaterialLineItemSerializer, MaterialSerializer, UnitSerializer


class MaterialLineItemViewSet(ModelViewSet):
    queryset = MaterialLineItem.objects.select_related('material_name', 'unit')\
        .order_by('date', 'location', 'material_name', '-quantity')\
        .all()

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


@api_view(['GET'])
def materiallineitems_csv_list(request, from_date, to_date):

    def validate(date_text):
        try:
            if date_text != datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
                raise ValueError
            return True
        except ValueError:
            return False
    if not (validate(from_date) and validate(to_date)):
        return Response("Wrong date format : it should be in YYYY-MM-DD", status=status.HTTP_400_BAD_REQUEST)

    from_date = datetime.strptime(from_date, "%Y-%m-%d")
    to_date = datetime.strptime(to_date, "%Y-%m-%d")
    diff = to_date - from_date
    if not 0 < diff.days < 365*2:
        return Response(f"Wrong date range, date range should in between 1 to 730 days", status=status.HTTP_400_BAD_REQUEST)

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(['Date', 'Material', 'Quantity', 'Unit', 'Location', 'Remarks'])

    for item in MaterialLineItem.objects \
        .filter(date__gte=from_date, date__lte=to_date) \
        .order_by('date', 'location', 'material_name', '-quantity').all():
        writer.writerow([item.date, item.material_name, item.quantity, item.unit, item.location, item.remarks])

    return response


