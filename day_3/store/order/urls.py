from django.urls import path
from django.db import router

from rest_framework.routers import DefaultRouter

from .views import OrderSet, OrderDetailSet, ComputerSet, MonitorSet, MouseSet, KeyboardSet

router = DefaultRouter()
router.register(r'mouses', MouseSet)
router.register(r'keyboards', KeyboardSet)
router.register(r'monitors', MonitorSet)
router.register(r'computers', ComputerSet)
router.register(r'orders', OrderSet)
router.register(r'orderdetails', OrderDetailSet)
urlpatterns = router.urls
