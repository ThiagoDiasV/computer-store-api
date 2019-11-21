from django.db import models
from django.contrib.auth.models import User


class Processor(models.Model):

    processor_choices = [
        ("Intel Core i5", "Intel Core i5"),
        ("Intel Core i7", "Intel Core i7"),
        ("AMD Athlon", "AMD Athlon"),
        ("AMD Ryzen 7", "AMD Ryzen 7"),
    ]

    processor_brands_choices = [("Intel", "Intel"), ("AMD", "AMD")]

    processor_description = models.CharField(
        max_length=30, choices=processor_choices
    )
    processor_brand = models.CharField(max_length=10, choices=processor_brands_choices)

    def __str__(self):
        return f"{self.processor_description}"


class MotherBoard(models.Model):
    motherboard_choices = [
        ("ASUS Prime", "Asus Prime"),
        ("Gigabyte", "Gigabyte"),
        ("ASRock Fatal", "ASRock Fatal"),
    ]

    supported_processors_choices = [
        ("Intel", "Intel"),
        ("AMD", "AMD"),
        ("Hybrid", "Hybrid"),
    ]

    slots_ram_choices = [(2, "2"), (4, "4")]

    max_ram_supported_choices = [(16, "16 GB"), (64, "64 GB")]

    motherboard_description = models.CharField(
        max_length=30, choices=motherboard_choices
    )
    supported_processors = models.CharField(
        max_length=10, choices=supported_processors_choices
    )
    slots_ram = models.PositiveIntegerField(choices=slots_ram_choices)
    max_ram_supported = models.PositiveIntegerField(choices=max_ram_supported_choices)
    integrated_graphic = models.BooleanField()

    def __str__(self):
        return f"{self.motherboard_description}"


class Memory(models.Model):
    memory_choices = [("Hiper X", "Hiper X")]

    sizes_choices = [(4, "4"), (8, "8"), (16, "16"), (32, "32"), (64, "64")]

    ram_description = models.CharField(max_length=10, choices=memory_choices)

    ram_size = models.PositiveIntegerField(choices=sizes_choices)

    def __str__(self):
        return f"{self.ram_description} {self.ram_size} GB"


class GraphicCard(models.Model):
    graphic_card_choices = [
        ("Gigabyte Geforce GTX 1060 6GB", "Gigabyte Geforce GTX 1060 6GB"),
        ("PNY RTX 2060 6GB", "PNY RTX 2060 6GB"),
        ("Radeon RX 580 8GB", "Radeon RX 580 8GB"),
    ]

    graphic_card_description = models.CharField(
        max_length=100, choices=graphic_card_choices
    )

    def __str__(self):
        return f"{self.graphic_card_description}"


class Computer(models.Model):
    processor_id = models.ForeignKey(Processor, on_delete=models.CASCADE)
    motherboard_id = models.ForeignKey(MotherBoard, on_delete=models.CASCADE)
    memory_id = models.ManyToManyField(Memory)
    graphic_card_id = models.ForeignKey(
        GraphicCard, on_delete=models.CASCADE, null=True, blank=False
    )


class Order(models.Model):
    computer_id = models.ManyToManyField(Computer)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
