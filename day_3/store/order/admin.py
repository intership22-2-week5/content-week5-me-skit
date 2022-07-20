from django.contrib import admin

from .models import Computer, Order, OrderDetails, Monitor, Mouse, Keyboard

admin.site.register(Computer)
admin.site.register(Order)
admin.site.register(OrderDetails)
admin.site.register(Monitor)
admin.site.register(Mouse)
admin.site.register(Keyboard)
