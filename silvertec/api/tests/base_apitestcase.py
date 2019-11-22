from rest_framework.test import APITestCase
from .base_testcase import BaseTestCase
from ..models import User, Processor, MotherBoard, Memory, GraphicCard


class BaseAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="intmed")
        self.url_processors = "/processors/"
        self.url_motherboards = "/motherboards/"
        self.url_computers = "/computers/"
        self.url_orders = "/orders/"
        self.client.force_authenticate(user=self.user)
        self.correct_processor_to_json = {
            "id": 1,
            "processor_description": "Intel Core i5",
            "processor_brand": "Intel",
        }
        self.wrong_processor_to_json = {
            "id": 2,
            "processor_description": "AMD Ryzen 7",
            "processor_brand": "Intel",
        }
        self.correct_motherboard_to_json = {
            "id": 1,
            "motherboard_description": "ASRock Fatal",
            "supported_processors": "Hybrid",
            "slots_ram": 4,
            "max_ram_supported": 64,
            "integrated_graphic": True,
        }
        self.wrong_motherboard_to_json = {
            "id": 2,
            "motherboard_description": "ASUS Prime",
            "supported_processors": "AMD",
            "slots_ram": 2,
            "max_ram_supported": 64,
            "integrated_graphic": True,
        }
        self.correct_computer_to_json = {
            "id": 1,
            "processor_id": Processor.objects.get(pk=1).id,
            "motherboard_id": MotherBoard.objects.get(pk=1).id,
            "memory_id": [Memory.objects.get(pk=1).id, Memory.objects.get(pk=2).id],
            "graphic_card_id": GraphicCard.objects.get(pk=1).id,
        }
