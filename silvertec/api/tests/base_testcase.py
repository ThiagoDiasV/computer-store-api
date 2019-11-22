from django.test import TestCase
from ..models import Processor, MotherBoard, Computer, Memory, GraphicCard


class BaseTestCase(TestCase):
    def setUp(self):
        self.intel_processor_1 = Processor(
            processor_description="Intel Core i5", processor_brand="Intel"
        )
        self.intel_processor_2 = Processor(
            processor_description="Intel Core i7", processor_brand="Intel"
        )
        self.amd_processor_1 = Processor(
            processor_description="AMD Ryzen 7", processor_brand="AMD"
        )
        self.amd_processor_2 = Processor(
            processor_description="AMD Athlon", processor_brand="AMD"
        )
        self.erroneous_intel_processor_1 = Processor(
            processor_description="Intel Core i5", processor_brand="AMD"
        )
        self.erroneous_amd_processor = Processor(
            processor_description="AMD Ryzen 7", processor_brand="Intel"
        )
        self.asus_motherboard = MotherBoard(
            motherboard_description="ASUS Prime",
            supported_processors="Intel",
            slots_ram=2,
            max_ram_supported=16,
            integrated_graphic=False,
        )
        self.gigabyte_motherboard = MotherBoard(
            motherboard_description="Gigabyte",
            supported_processors="AMD",
            slots_ram=2,
            max_ram_supported=16,
            integrated_graphic=False,
        )
        self.asrock_motherboard = MotherBoard(
            motherboard_description="ASRock Fatal",
            supported_processors="Hybrid",
            slots_ram=4,
            max_ram_supported=64,
            integrated_graphic=True,
        )
        self.erroneous_asus_motherboard = MotherBoard(
            motherboard_description="ASUS Prime",
            supported_processors="AMD",
            slots_ram=2,
            max_ram_supported=16,
            integrated_graphic=False,
        )
        self.erroneous_gigabyte_motherboard = MotherBoard(
            motherboard_description="Gigabyte",
            supported_processors="AMD",
            slots_ram=4,
            max_ram_supported=16,
            integrated_graphic=False,
        )
        self.erroneous_asrock_motherboard = MotherBoard(
            motherboard_description="ASRock Fatal",
            supported_processors="Hybrid",
            slots_ram=4,
            max_ram_supported=16,
            integrated_graphic=False,
        )
        self.ram4gb = Memory(ram_description="Hiper X", ram_size=4)
        self.ram8gb = Memory(ram_description="Hiper X", ram_size=8)
        self.ram16gb = Memory(ram_description="Hiper X", ram_size=16)
        self.ram32gb = Memory(ram_description="Hiper X", ram_size=32)
        self.ram64gb = Memory(ram_description="Hiper X", ram_size=64)
        self.geforce_graphic_card = GraphicCard(
            graphic_card_description="Gigabyte Geforce GTX 1060 6GB"
        )
        self.pnyrtx_graphic_card = GraphicCard(
            graphic_card_description="PNY RTX 2060 6GB"
        )
        self.radeonrx_graphic_card = GraphicCard(
            graphic_card_description="Radeon RX 580 8GB"
        )
        self.asus_computer = Computer(
            1,
            self.intel_processor_1,
            self.asus_motherboard,
            self.geforce_graphic_card,
        )
        self.asus_computer_2 = Computer(
            2, self.intel_processor_2, self.asus_motherboard, None
        )
        self.gigabyte_computer = Computer(
            3,
            self.amd_processor_1,
            self.gigabyte_motherboard,
            self.radeonrx_graphic_card,
        )
        self.asrock_computer = Computer(
            4, self.intel_processor_1, self.asrock_motherboard, GraphicCard()
        )
        self.erroneous_asus_computer = Computer(
            5, self.amd_processor_1, self.asus_motherboard, GraphicCard()
        )
        self.erroneous_gigabyte_computer = Computer(
            6, self.intel_processor_1, self.gigabyte_motherboard, GraphicCard()
        )
        self.erroneous_asrock_computer = Computer(
            7,
            self.intel_processor_2,
            self.asrock_motherboard,
            self.geforce_graphic_card,
        )
