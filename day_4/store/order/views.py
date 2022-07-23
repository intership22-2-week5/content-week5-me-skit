
from django import views
from django.shortcuts import render
from rest_framework.views import Response
from rest_framework import viewsets

from .models import Keyboard, Mouse, Display, Speaker, Motherboard, Processor, Computer, Order, OrderDetails
from .serializers import KeyboardSerializer, MouseSerializer, DisplaySerializer, SpeakerSerializer, MotherboardSerializer, ProcessorSerializer, ComputerSerializer, OrderSerializer, OrderDetailSerializer

class KeyboardSet(viewsets.ModelViewSet):
    queryset = Keyboard.objects.all()
    serializer_class = KeyboardSerializer 


class MouseSet(viewsets.ModelViewSet):
    queryset = Mouse.objects.all()
    serializer_class = MouseSerializer

class DisplaySet(viewsets.ModelViewSet):
    queryset = Display.objects.all()
    serializer_class = DisplaySerializer

class SpeakerSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

class MotherboardSet(viewsets.ModelViewSet):
    queryset = Motherboard.objects.all()
    serializer_class = MotherboardSerializer

class ProcessorSet(viewsets.ModelViewSet):
    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer


class ComputerSet(viewsets.ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.data['id']:
            return response
        
        return Response({ 'message': 'Not enough stock' })

class OrderSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # def create(self, request, *args, **kwargs):
    #     response = super().create(request, *args, **kwargs)
    #     if response.data['id']:
    #         return response
        
    #     return Response({ 'message': 'Not enough stock' })    


class OrderDetailSet(viewsets.ModelViewSet):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.data['id']:
            return response
        
        return Response({ 'message': 'Not enough stock' })   