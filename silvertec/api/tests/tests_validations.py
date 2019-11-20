from .base_testcase import BaseTestCase
from ..validations import validate_processor, validate_motherboard, validate_computer_components
from ..serializers import (
    ProcessorSerializer,
    MotherBoardSerializer,
    ComputerSerializer,
    MemorySerializer,
)
from rest_framework.serializers import ValidationError


class TestProcessorValidationFunction(BaseTestCase):
    def setUp(self):
        super(TestProcessorValidationFunction, self).setUp()

    def test_processor_validation_function(self):
        serializer_1 = ProcessorSerializer(self.erroneous_amd_processor)
        serializer_2 = ProcessorSerializer(self.erroneous_intel_processor_1)
        self.assertRaises(ValidationError, validate_processor, serializer_1.data)
        self.assertRaises(ValidationError, validate_processor, serializer_2.data)


class TestMotherBoardValidationFunction(BaseTestCase):
    def setUp(self):
        super(TestMotherBoardValidationFunction, self).setUp()

    def test_motherboard_validation_function(self):
        serializer_1 = MotherBoardSerializer(self.erroneous_asus_motherboard)
        serializer_2 = MotherBoardSerializer(self.erroneous_gigabyte_motherboard)
        serializer_3 = MotherBoardSerializer(self.erroneous_asrock_motherboard)
        self.assertRaises(ValidationError, validate_motherboard, serializer_1.data)
        self.assertRaises(ValidationError, validate_motherboard, serializer_2.data)
        self.assertRaises(ValidationError, validate_motherboard, serializer_3.data)