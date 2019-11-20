from ..serializers import (
    ProcessorSerializer,
    MotherBoardSerializer,
    ComputerSerializer,
    MemorySerializer,
)
from .base_testcase import BaseTestCase


class TestModelProcessor(BaseTestCase):
    def setUp(self) -> None:
        super(TestModelProcessor, self).setUp()

    def test_if_processor_is_an_Intel_then_AMD_brand_is_not_allowed(self):
        serializer = ProcessorSerializer(self.intel_processor_1)
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


class TestModelMotherBoard(BaseTestCase):
    def setUp(self) -> None:
        super(TestModelMotherBoard, self).setUp()

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


class TestModelComputer(BaseTestCase):
    def setUp(self) -> None:
        super(TestModelComputer, self).setUp()

    def test_asus_computer_components(self):
        computer_serializer = ComputerSerializer(self.asus_computer)
        memory_1_serializer = MemorySerializer(self.ram8gb)
        memory_2_serializer = MemorySerializer(self.ram8gb)

        total_ram = sum(
            (memory_1_serializer.data["RAM_size"], memory_2_serializer.data["RAM_size"])
        )

        self.assertIn("Intel", str(computer_serializer.data["processor_id"]))
        self.assertLessEqual(total_ram, 16)
        self.assertTrue(str(computer_serializer.data["video_card_id"]))

    def test_gigabyte_computer_components(self):
        computer_serializer = ComputerSerializer(self.gigabyte_computer)
        memory_1_serializer = MemorySerializer(self.ram4gb)
        memory_2_serializer = MemorySerializer(self.ram4gb)
        memory_3_serializer = MemorySerializer(self.ram4gb)

        total_ram = sum(
            (memory_1_serializer.data["RAM_size"], memory_2_serializer.data["RAM_size"])
        )
        total_ram_cards = len(
            (
                memory_1_serializer,
                memory_2_serializer,
                memory_3_serializer
            )
        )

        self.assertIn("AMD", str(computer_serializer.data["processor_id"]))
        self.assertLessEqual(total_ram, 16)
        self.assertTrue(str(computer_serializer.data["video_card_id"]))
        self.assertGreater(total_ram_cards, 2)

    def test_asrock_computer_components(self):
        computer_serializer = ComputerSerializer(self.asrock_computer)
        memory_1_serializer = MemorySerializer(self.ram32gb)
        memory_2_serializer = MemorySerializer(self.ram32gb)

        total_ram = sum(
            (memory_1_serializer.data["RAM_size"], memory_2_serializer.data["RAM_size"])
        )

        self.assertIn("Intel", str(computer_serializer.data["processor_id"]))
        self.assertLessEqual(total_ram, 64)
        self.assertFalse(str(computer_serializer.data["video_card_id"]))
