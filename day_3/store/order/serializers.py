from rest_framework import serializers
from .models import Order, Computer, Monitor, Mouse, Keyboard, OrderDetails


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        exclude = ['devise']


class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        exclude = ['devise']


class MouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mouse
        exclude = ['devise']


class KeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyboard
        exclude = ['devise']
