from rest_framework import viewsets
from .models import Order, OrderDetails, Computer, Monitor, Mouse, Keyboard
from .serializers import OrderSerializer, OrderDetailSerializer, ComputerSerializer, MonitorSerializer, MouseSerializer, KeyboardSerializer

class OrderSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailSet(viewsets.ModelViewSet):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailSerializer


class ComputerSet(viewsets.ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer


class MonitorSet(viewsets.ModelViewSet):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer

class MouseSet(viewsets.ModelViewSet):
    queryset = Mouse.objects.all()
    serializer_class = MouseSerializer


class KeyboardSet(viewsets.ModelViewSet):
    queryset = Keyboard.objects.all()
    serializer_class = KeyboardSerializer