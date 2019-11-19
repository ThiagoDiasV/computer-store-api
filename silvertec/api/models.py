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

    processor_description = models.CharField(max_length=30, choices=processor_choices)
    processor_brand = models.CharField(max_length=10, choices=processor_brands_choices)

    def __str__(self):
        return f"{self.processor_description}"


class MotherBoard(models.Model):
    motherboard_choices = [
        ("ASUS Prime", "Asus Prime"),
        ("Gigabyte", "Gigabyte"),
        ("ASRock Fatal", "ASRock Fatal")
    ]

    supported_processors_choices = [
        ("Intel", "Intel"),
        ("AMD", "AMD"),
        ("Hybrid", "Hybrid")
    ]

    slots_RAM_choices = [(2, "2"), (4, "4")]

    max_RAM_supported_choices = [(16, "16 GB"), (64, "64 GB")]

    motherboard_description = models.CharField(
        max_length=30, choices=motherboard_choices
    )
    supported_processors = models.CharField(
        max_length=10, choices=supported_processors_choices
    )
    slots_RAM = models.PositiveIntegerField(choices=slots_RAM_choices)
    max_RAM_supported = models.PositiveIntegerField(choices=max_RAM_supported_choices)
    integrated_video = models.BooleanField()

    def __str__(self):
        return f"{self.motherboard_description}"


class Memory(models.Model):
    memory_choices = [("Hiper X", "Hiper X")]

    sizes_choices = [(4, "4"), (8, "8"), (16, "16"), (32, "32"), (64, "64")]

    RAM_description = models.CharField(max_length=10, choices=memory_choices)

    RAM_size = models.PositiveIntegerField(choices=sizes_choices)

    def __str__(self):
        return self.RAM_description


class VideoCard(models.Model):
    video_card_choices = [
        ("Gigabyte Geforce GTX 1060 6GB", "Gigabyte Geforce GTX 1060 6GB"),
        ("PNY RTX 2060 6GB", "PNY RTX 2060 6GB"),
        ("Radeon RX 580 8GB", "Radeon RX 580 8GB"),
    ]

    video_card_description = models.CharField(
        max_length=100, choices=video_card_choices
    )

    def __str__(self):
        return self.video_card_description


class Computer(models.Model):
    processor_id = models.ForeignKey(Processor, on_delete=models.CASCADE)
    motherboard_id = models.ForeignKey(MotherBoard, on_delete=models.CASCADE)
    memory_id = models.ManyToManyField(Memory)
    video_card_id = models.ForeignKey(VideoCard, on_delete=models.CASCADE)


class Order(models.Model):
    computer_id = models.ManyToManyField(Computer)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
