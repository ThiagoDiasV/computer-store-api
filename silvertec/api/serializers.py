from rest_framework import serializers
from .models import Processor, MotherBoard, Memory, GraphicCard, User, Order, Computer
from .validations import (
    validate_processor,
    validate_motherboard,
    validate_processor_compatibility_with_motherboard,
    validate_memory_cards_and_motherboard_ram_slots,
)


class ProcessorSerializer(serializers.ModelSerializer):
    def validate(self, data):
        validate_processor(data)
        return data

    class Meta:
        model = Processor
        fields = "__all__"


class MotherBoardSerializer(serializers.ModelSerializer):
    def validate(self, data):
        validate_motherboard(data)
        return data

    class Meta:
        model = MotherBoard
        fields = "__all__"


class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = "__all__"


class GraphicCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraphicCard
        fields = "__all__"


class ComputerSerializer(serializers.ModelSerializer):
    def validate(self, data):
        validate_processor_compatibility_with_motherboard(data)
        validate_memory_cards_and_motherboard_ram_slots(data)
        return data

    class Meta:
        model = Computer
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
