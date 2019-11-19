from rest_framework import serializers
from .models import Processor, MotherBoard, Memory, VideoCard, User, Order
from .validations import validate_processor, validate_motherboard


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


class VideoCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCard
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
