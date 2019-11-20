from rest_framework import serializers
from .models import Processor, MotherBoard, Memory, GraphicCard, User, Order, Computer
from .validations import (
    validate_processor, validate_motherboard, validate_asus_computer_components
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
        validate_asus_computer_components(data)
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
