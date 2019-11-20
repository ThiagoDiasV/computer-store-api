from .base_testcase import BaseTestCase
from ..validations import (
    validate_processor,
    validate_motherboard,
    validate_asus_computer_components,
)
from ..serializers import (
    ProcessorSerializer,
    MotherBoardSerializer,
    ComputerSerializer,
    MemorySerializer,
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

    def test_asus_mb_computer_validation_function(self):
        erroneous_computer_serializer = ComputerSerializer(self.erroneous_asus_computer)
        memory_1 = self.ram8gb
        memory_2 = self.ram8gb
        memory_3 = self.ram8gb
        list_of_memories = [memory_1, memory_2, memory_3]

        for memory in list_of_memories:
            erroneous_computer_serializer.data["memory_id"].append(memory)
        self.assertRaises(
            ValidationError,
            validate_asus_computer_components,
            erroneous_computer_serializer.data,
        )
