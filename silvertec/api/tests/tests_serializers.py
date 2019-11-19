from django.test import TestCase
from ..serializers import (
    ProcessorSerializer,
    MotherBoardSerializer,
    ComputerSerializer,
    MemorySerializer,
    VideoCardSerializer,
)
from ..models import Processor, MotherBoard, Computer, Memory, VideoCard
from model_bakery import baker


class TestModelProcessor(TestCase):
    def setUp(self) -> None:
        self.intel_processor = Processor(
            processor_description="Intel Core i5", processor_brand="Intel"
        )
        self.amd_processor_1 = Processor(
            processor_description="AMD Ryzen 7", processor_brand="AMD"
        )
        self.amd_processor_2 = Processor(
            processor_description="AMD Athlon", processor_brand="AMD"
        )

    def test_if_processor_is_an_Intel_then_AMD_brand_is_not_allowed(self):
        serializer = ProcessorSerializer(self.intel_processor)
        description = serializer.data["processor_description"]
        brand = serializer.data["processor_brand"]
        self.assertIn("Intel", description)
        self.assertIn("Intel", brand)

    def test_if_processor_is_an_AMD_then_Intel_brand_is_not_allowed(self):
        serializer_1 = ProcessorSerializer(self.amd_processor_1)
        serializer_2 = ProcessorSerializer(self.amd_processor_2)
        result_1 = serializer_1.data["processor_description"]
        result_2 = serializer_2.data["processor_description"]
        self.assertIn("AMD", result_1)
        self.assertIn("Athlon", result_2)


class TestModelMotherBoard(TestCase):
    def setUp(self) -> None:
        self.asus_motherboard = MotherBoard(
            motherboard_description="ASUS Prime",
            supported_processors="Intel",
            slots_RAM=2,
            max_RAM_supported=16,
            integrated_video=False,
        )
        self.gigabyte_motherboard = MotherBoard(
            motherboard_description="Gigabyte",
            supported_processors="AMD",
            slots_RAM=2,
            max_RAM_supported=16,
            integrated_video=False,
        )
        self.asrock_motherboard = MotherBoard(
            motherboard_description="ASRock Fatal",
            supported_processors="Hybrid",
            slots_RAM=4,
            max_RAM_supported=64,
            integrated_video=True,
        )

    def test_if_ASUS_mb_is_correctly_set(self):
        serializer = MotherBoardSerializer(self.asus_motherboard)
        description = serializer.data["motherboard_description"]
        supported_processor = serializer.data["supported_processors"]
        slots_RAM = serializer.data["slots_RAM"]
        max_RAM = serializer.data["max_RAM_supported"]
        integrated_video = serializer.data["integrated_video"]
        self.assertIn("ASUS", description)
        self.assertIn("Intel", supported_processor)
        self.assertEqual(2, slots_RAM)
        self.assertEqual(16, max_RAM)
        self.assertFalse(integrated_video)

    def test_if_gigabyte_mb_is_correctly_set(self):
        serializer = MotherBoardSerializer(self.gigabyte_motherboard)
        description = serializer.data["motherboard_description"]
        supported_processor = serializer.data["supported_processors"]
        slots_RAM = serializer.data["slots_RAM"]
        max_RAM = serializer.data["max_RAM_supported"]
        integrated_video = serializer.data["integrated_video"]
        self.assertIn("Gigabyte", description)
        self.assertIn("AMD", supported_processor)
        self.assertEqual(2, slots_RAM)
        self.assertEqual(16, max_RAM)
        self.assertFalse(integrated_video)

    def test_if_asrock_mb_is_correctly_set(self):
        serializer = MotherBoardSerializer(self.asrock_motherboard)
        description = serializer.data["motherboard_description"]
        supported_processor = serializer.data["supported_processors"]
        slots_RAM = serializer.data["slots_RAM"]
        max_RAM = serializer.data["max_RAM_supported"]
        integrated_video = serializer.data["integrated_video"]
        self.assertIn("ASRock", description)
        self.assertIn("Hybrid", supported_processor)
        self.assertEqual(4, slots_RAM)
        self.assertEqual(64, max_RAM)
        self.assertTrue(integrated_video)


class TestModelComputer(TestCase):
    def setUp(self):
        """
        Here is a class TestComputer to use in our
        configurations compatibilities tests.
        """
        class TestComputer:
            def __init__(self, processor, mb, ram, videocard):
                self.processor = processor
                self.mb = mb
                self.ram = ram
                self.videocard = videocard
                
        self.test_computer_1 = TestComputer(
            processor=Processor(
                processor_description="Intel Core i5", processor_brand="Intel"
            ),
            mb=MotherBoard(
                motherboard_description="ASUS Prime",
                supported_processors="Intel",
                slots_RAM=2,
                max_RAM_supported=16,
                integrated_video=False,
            ),
            videocard=VideoCard(),
            ram=[
                Memory(RAM_description="Hiper X", RAM_size=4),
                Memory(RAM_description="Hiper X", RAM_size=4),
            ],
        )
        self.bunch_of_computers = baker.make(Computer, _quantity=10, make_m2m=True)

    def test_asus_mb_computer_processor_intel_2_slots_16_max_ram_no_video(self):
        self.assertEqual(self.test_computer_1.mb.motherboard_description, "ASUS Prime")
        self.assertIn("Intel", self.test_computer_1.processor.processor_description)
        self.assertFalse(self.test_computer_1.videocard.video_card_description)
        self.assertEqual(len(self.test_computer_1.ram), 2)
