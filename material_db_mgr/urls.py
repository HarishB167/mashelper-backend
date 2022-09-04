from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('materiallineitem', views.MaterialLineItemViewSet)

urlpatterns = router.urls
