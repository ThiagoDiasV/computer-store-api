from rest_framework import serializers
from .models import (
    Processor,
    MotherBoard,
    Memory,
    GraphicCard,
    User,
    Order,
    Computer,
)
from .validations import (
    validate_processor,
    validate_motherboard,
    validate_processor_compatibility_with_motherboard,
    validate_memory_cards_and_motherboard_ram_slots,
    validate_total_ram_ordered_and_motherboard_ram_support,
    validate_graphic_card_or_not_in_motherboard,
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
        validate_total_ram_ordered_and_motherboard_ram_support(data),
        validate_graphic_card_or_not_in_motherboard(data)
        return data

    class Meta:
        model = Computer
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)
        user_id = serializers.ReadOnlyField(source="user_id.username")


class OrderSerializer(serializers.ModelSerializer):
    def validate(self, data):
        # from ipdb import set_trace; set_trace()
        return data

    class Meta:
        model = Order
        fields = "__all__"
