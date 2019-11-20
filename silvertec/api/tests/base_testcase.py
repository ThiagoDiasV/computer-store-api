from django.test import TestCase
from ..models import Processor, MotherBoard, Computer, Memory, VideoCard


class BaseTestCase(TestCase):
    def setUp(self):
        self.intel_processor_1= Processor(
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
        self.erroneous_intel_processor_1= Processor(
            processor_description="Intel Core i5", processor_brand="AMD"
        )
        self.erroneous_amd_processor = Processor(
            processor_description="AMD Ryzen 7", processor_brand="Intel"
        )
        self.asus_motherboard = MotherBoard(
            motherboard_description="ASUS Prime",
            supported_processors="Intel",
            slots_RAM=2,
            max_RAM_supported=16,
            integrated_video=False
        )
        self.gigabyte_motherboard = MotherBoard(
            motherboard_description="Gigabyte",
            supported_processors="AMD",
            slots_RAM=2,
            max_RAM_supported=16,
            integrated_video=False
        )
        self.asrock_motherboard = MotherBoard(
            motherboard_description="ASRock Fatal",
            supported_processors="Hybrid",
            slots_RAM=4,
            max_RAM_supported=64,
            integrated_video=True
        )
        self.erroneous_asus_motherboard = MotherBoard(
            motherboard_description="ASUS Prime",
            supported_processors="AMD",
            slots_RAM=2,
            max_RAM_supported=16,
            integrated_video=False
        )
        self.erroneous_gigabyte_motherboard = MotherBoard(
            motherboard_description="Gigabyte",
            supported_processors="AMD",
            slots_RAM=4,
            max_RAM_supported=16,
            integrated_video=False
        )
        self.erroneous_asrock_motherboard = MotherBoard(
            motherboard_description="ASRock Fatal",
            supported_processors="Hybrid",
            slots_RAM=4,
            max_RAM_supported=16,
            integrated_video=False
        )
        self.ram4gb = Memory(RAM_description="Hiper X", RAM_size=4)
        self.ram8gb = Memory(RAM_description="Hiper X", RAM_size=8)
        self.ram16gb = Memory(RAM_description="Hiper X", RAM_size=16)
        self.ram32gb = Memory(RAM_description="Hiper X", RAM_size=32)
        self.ram64gb = Memory(RAM_description="Hiper X", RAM_size=64)
        self.geforce_video_card = VideoCard(
            video_card_description="Gigabyte Geforce GTX 1060 6GB"
        )
        self.pnyrtx_video_card = VideoCard(video_card_description="PNY RTX 2060 6GB")
        self.radeonrx_video_card = VideoCard(video_card_description="Radeon RX 580 8GB")
        self.asus_computer = Computer(
            1, self.intel_processor_1, self.asus_motherboard, self.geforce_video_card
        )
        self.gigabyte_computer = Computer(
            2, self.amd_processor_1, self.gigabyte_motherboard, self.pnyrtx_video_card
        )
        self.asrock_computer = Computer(
            3, self.intel_processor_1, self.asrock_motherboard, VideoCard()
        )
