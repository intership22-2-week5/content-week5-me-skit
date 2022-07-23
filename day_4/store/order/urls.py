from django.urls import path
from django.db import router

from rest_framework.routers import DefaultRouter

from .views import KeyboardSet, MouseSet, DisplaySet, SpeakerSet, MotherboardSet, ProcessorSet, ComputerSet, OrderSet, OrderDetailSet

router = DefaultRouter()
router.register(r'keyboards', KeyboardSet)
router.register(r'mouses', MouseSet)
router.register(r'monitors', DisplaySet)
router.register(r'speakers', SpeakerSet)
router.register(r'motherboards', MotherboardSet)
router.register(r'processors', ProcessorSet)
router.register(r'computers', ComputerSet)
router.register(r'orders', OrderSet)
router.register(r'orderdetails', OrderDetailSet)
urlpatterns = router.urls

urlpatterns += []