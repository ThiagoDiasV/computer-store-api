from rest_framework.test import APITestCase
from .base_testcase import BaseTestCase
from ..models import User, Processor, MotherBoard, Memory, GraphicCard


class BaseAPITestCase(APITestCase, BaseTestCase):
    def setUp(self):
        super().setUp()
        self.user = User.objects.create(username="intmed")
        self.url_processors = "/processors/"
        self.url_motherboards = "/motherboards/"
        self.url_computers = "/computers/"
        self.url_orders = "/orders/"
        self.client.force_authenticate(user=self.user)
        self.correct_processor_to_json = {
            "id": 5,
            "processor_description": "Intel Core i5",
            "processor_brand": "Intel",
        }
        self.wrong_processor_to_json = {
            "id": 6,
            "processor_description": "AMD Ryzen 7",
            "processor_brand": "Intel",
        }
        self.correct_motherboard_to_json = {
            "id": 4,
            "motherboard_description": "ASRock Fatal",
            "supported_processors": "Hybrid",
            "slots_ram": 4,
            "max_ram_supported": 64,
            "integrated_graphic": True,
        }
        self.wrong_motherboard_to_json = {
            "id": 5,
            "motherboard_description": "ASUS Prime",
            "supported_processors": "AMD",
            "slots_ram": 2,
            "max_ram_supported": 64,
            "integrated_graphic": True,
        }
        self.correct_computer_to_json = {
            "id": 1,
            "processor_id": Processor.objects.all()
            .filter(processor_description="Intel Core i5")
            .first()
            .id,
            "motherboard_id": MotherBoard.objects.all()
            .filter(supported_processors="Intel")
            .first()
            .id,
            "memory_id": [
                Memory.objects.all().filter(ram_size=8).first().id,
                Memory.objects.all().filter(ram_size=8).first().id,
            ],
            "graphic_card_id": GraphicCard.objects.all()
            .filter(graphic_card_description="Radeon RX 580 8GB")
            .first()
            .id,
        }
        self.wrong_computer_to_json = {
            "id": 2,
            "processor_id": Processor.objects.all()
            .filter(processor_description="Intel Core i5")
            .first()
            .id,
            "motherboard_id": MotherBoard.objects.all()
            .filter(supported_processors="AMD")
            .first()
            .id,
            "memory_id": [
                Memory.objects.all().filter(ram_size=8).first().id,
                Memory.objects.all().filter(ram_size=8).first().id,
            ],
            "graphic_card_id": GraphicCard.objects.all()
            .filter(graphic_card_description="Radeon RX 580 8GB")
            .first()
            .id,
        }
        self.first_computer_id_to_json = {"id": 1, "computer_id": 1}
