from rest_framework import serializers
from .models import Keyboard, Mouse, Display, Speaker, Motherboard, Processor, Computer, Order


class KeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyboard
        fields = '__all__'


class MouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mouse
        fields = '__all__'


class DisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Display
        fields = '__all__'


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = '__all__'


class MotherboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motherboard
        fields = '__all__'


class ProcessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processor
        fields = '__all__'


class ComputerSerializer(serializers.ModelSerializer):
    keyboard = serializers.PrimaryKeyRelatedField(queryset = Keyboard.objects.all())
    mouse = serializers.PrimaryKeyRelatedField(queryset = Mouse.objects.all())
    display = serializers.PrimaryKeyRelatedField(queryset = Display.objects.all())
    speaker = serializers.PrimaryKeyRelatedField(queryset = Speaker.objects.all())
    motherboard = serializers.PrimaryKeyRelatedField(queryset = Motherboard.objects.all())
    processor = serializers.PrimaryKeyRelatedField(queryset = Processor.objects.all())

    class Meta:
        model = Computer
        # exclude = ['total_cost']
        fields = ['id', 'name', 'quantity', 'keyboard', 'mouse', 'display', 'speaker', 'motherboard', 'processor', 'created_at', 'updated_at']


class OrderSerializer(serializers.ModelSerializer):
    computer = serializers.PrimaryKeyRelatedField(queryset = Computer.objects.all())

    class Meta:
        model = Order
        # fields = '__all__'
        fields = ['id', 'quantity', 'computer', 'created_at', 'updated_at']
