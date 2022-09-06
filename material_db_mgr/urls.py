from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('materiallineitem', views.MaterialLineItemViewSet)
router.register('material', views.MaterialViewSet)
router.register('unit', views.UnitViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('materiallineitems/', views.materiallineitem_list, name='materiallineitem-listcreate'),
    path('materiallineitems_csv/<from_date>/<to_date>/', views.materiallineitems_csv_list, name='materiallineitem-getcsvlist'),
]
