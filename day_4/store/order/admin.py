from django.contrib import admin

from .models import Keyboard, Mouse, Display, Speaker, Motherboard, Processor, Computer, Order

admin.site.register(Keyboard)
admin.site.register(Mouse)
admin.site.register(Display)
admin.site.register(Speaker)
admin.site.register(Motherboard)
admin.site.register(Processor)
admin.site.register(Computer)
admin.site.register(Order)
