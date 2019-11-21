from django.contrib import admin
from .models import Processor, MotherBoard, Memory, GraphicCard, Order, Computer


admin.site.register(Processor)
admin.site.register(MotherBoard)
admin.site.register(Memory)
admin.site.register(GraphicCard)
admin.site.register(Computer)
admin.site.register(Order)
