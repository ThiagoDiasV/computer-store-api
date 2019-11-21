from .base_testcase import BaseTestCase
from ..validations import (
    validate_processor,
    validate_motherboard,
    validate_processor_compatibility_with_motherboard,
    validate_memory_cards_and_motherboard_ram_slots
)
from ..serializers import (
    ProcessorSerializer,
    MotherBoardSerializer,
    ComputerSerializer,
    MemorySerializer
)
from rest_framework.serializers import ValidationError


class TestProcessorValidationFunction(BaseTestCase):
    """
    Test class to validate the validate_processor function.
    """

    def setUp(self):
        super(TestProcessorValidationFunction, self).setUp()

    def test_processor_validation_function(self):
        serializer_1 = ProcessorSerializer(self.erroneous_amd_processor)
        serializer_2 = ProcessorSerializer(self.erroneous_intel_processor_1)
        self.assertRaises(ValidationError, validate_processor, serializer_1.data)
        self.assertRaises(ValidationError, validate_processor, serializer_2.data)


class TestMotherBoardValidationFunction(BaseTestCase):
    """
    Test class to validate the validate_motherboard function.
    """

    def setUp(self):
        super(TestMotherBoardValidationFunction, self).setUp()

    def test_motherboard_validation_function(self):
        serializer_1 = MotherBoardSerializer(self.erroneous_asus_motherboard)
        serializer_2 = MotherBoardSerializer(self.erroneous_gigabyte_motherboard)
        serializer_3 = MotherBoardSerializer(self.erroneous_asrock_motherboard)
        self.assertRaises(ValidationError, validate_motherboard, serializer_1.data)
        self.assertRaises(ValidationError, validate_motherboard, serializer_2.data)
        self.assertRaises(ValidationError, validate_motherboard, serializer_3.data)


class TestComputerValidationsFunctions(BaseTestCase):
    """
    Test class to validate the functions which validates computer build.
    """

    def setUp(self):
        super(TestComputerValidationsFunctions, self).setUp()

    def test_if_processor_is_compatible_with_motherboard(self):
        asus_mb_with_amd_processor_computer = ComputerSerializer(
                self.erroneous_asus_computer
            )
        gigabyte_mb_with_intel_processor_computer = ComputerSerializer(
                self.erroneous_gigabyte_computer
            )

        self.assertRaises(
                ValidationError,
                validate_processor_compatibility_with_motherboard,
                asus_mb_with_amd_processor_computer.data
            )
        self.assertRaises(
                ValidationError,
                validate_processor_compatibility_with_motherboard,
                gigabyte_mb_with_intel_processor_computer.data
            )

    def test_if_number_of_ram_cards_is_compatible_with_motherboard(self):
        asus_computer = ComputerSerializer(self.asus_computer)
        asrock_computer = ComputerSerializer(self.asrock_computer)

        memories_list = [MemorySerializer(self.ram4gb) for memory in range(5)]

        for memory in memories_list[:3]:
            asus_computer.data['memory_id'].append(memory.data)

        for memory in memories_list:
            asrock_computer.data['memory_id'].append(memory.data)

        self.assertRaises(
                ValidationError,
                validate_memory_cards_and_motherboard_ram_slots,
                asus_computer.data
            )
        self.assertRaises(
            ValidationError,
            validate_memory_cards_and_motherboard_ram_slots,
            asrock_computer.data
        )
