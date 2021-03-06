from ..serializers import (
    ProcessorSerializer,
    MotherBoardSerializer,
    ComputerSerializer,
    MemorySerializer,
)
from .base_testcase import BaseTestCase


class TestModelProcessor(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()

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
        super().setUp()

    def test_if_ASUS_mb_is_correctly_set(self):
        serializer = MotherBoardSerializer(self.asus_motherboard)
        description = serializer.data["motherboard_description"]
        supported_processor = serializer.data["supported_processors"]
        slots_ram = serializer.data["slots_ram"]
        max_ram = serializer.data["max_ram_supported"]
        integrated_graphic = serializer.data["integrated_graphic"]
        self.assertIn("ASUS", description)
        self.assertIn("Intel", supported_processor)
        self.assertEqual(2, slots_ram)
        self.assertEqual(16, max_ram)
        self.assertFalse(integrated_graphic)

    def test_if_gigabyte_mb_is_correctly_set(self):
        serializer = MotherBoardSerializer(self.gigabyte_motherboard)
        description = serializer.data["motherboard_description"]
        supported_processor = serializer.data["supported_processors"]
        slots_ram = serializer.data["slots_ram"]
        max_ram = serializer.data["max_ram_supported"]
        integrated_graphic = serializer.data["integrated_graphic"]
        self.assertIn("Gigabyte", description)
        self.assertIn("AMD", supported_processor)
        self.assertEqual(2, slots_ram)
        self.assertEqual(16, max_ram)
        self.assertFalse(integrated_graphic)

    def test_if_asrock_mb_is_correctly_set(self):
        serializer = MotherBoardSerializer(self.asrock_motherboard)
        description = serializer.data["motherboard_description"]
        supported_processor = serializer.data["supported_processors"]
        slots_ram = serializer.data["slots_ram"]
        max_ram = serializer.data["max_ram_supported"]
        integrated_graphic = serializer.data["integrated_graphic"]
        self.assertIn("ASRock", description)
        self.assertIn("Hybrid", supported_processor)
        self.assertEqual(4, slots_ram)
        self.assertEqual(64, max_ram)
        self.assertTrue(integrated_graphic)


class TestModelComputer(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()

    def test_asus_computer_components(self):
        computer_serializer = ComputerSerializer(self.asus_computer)
        memory_1_serializer = MemorySerializer(self.ram8gb)
        memory_2_serializer = MemorySerializer(self.ram8gb)

        total_ram = sum(
            (
                memory_1_serializer.data["ram_size"],
                memory_2_serializer.data["ram_size"],
            )
        )

        self.assertIn("Intel", str(computer_serializer.data["processor_id"]))
        self.assertLessEqual(total_ram, 16)
        self.assertTrue(str(computer_serializer.data["graphic_card_id"]))

    def test_gigabyte_computer_components(self):
        computer_serializer = ComputerSerializer(self.gigabyte_computer)
        memory_1_serializer = MemorySerializer(self.ram4gb)
        memory_2_serializer = MemorySerializer(self.ram4gb)
        memory_3_serializer = MemorySerializer(self.ram4gb)

        total_ram = sum(
            (
                memory_1_serializer.data["ram_size"],
                memory_2_serializer.data["ram_size"],
            )
        )
        total_ram_cards = len(
            (memory_1_serializer, memory_2_serializer, memory_3_serializer,)
        )

        self.assertIn("AMD", str(computer_serializer.data["processor_id"]))
        self.assertLessEqual(total_ram, 16)
        self.assertTrue(str(computer_serializer.data["graphic_card_id"]))
        self.assertGreater(total_ram_cards, 2)

    def test_asrock_computer_components(self):
        computer_serializer = ComputerSerializer(self.asrock_computer)
        memory_1_serializer = MemorySerializer(self.ram32gb)
        memory_2_serializer = MemorySerializer(self.ram32gb)

        total_ram = sum(
            (
                memory_1_serializer.data["ram_size"],
                memory_2_serializer.data["ram_size"],
            )
        )

        self.assertIn("Intel", str(computer_serializer.data["processor_id"]))
        self.assertLessEqual(total_ram, 64)
        self.assertFalse(str(computer_serializer.data["graphic_card_id"]))
