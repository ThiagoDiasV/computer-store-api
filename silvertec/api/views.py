from .models import Processor, MotherBoard, Memory, GraphicCard, Computer, Order, User
from .serializers import (
    ProcessorSerializer,
    MotherBoardSerializer,
    MemorySerializer,
    GraphicCardSerializer,
    ComputerSerializer,
    UserSerializer,
    OrderSerializer
)
from rest_framework import generics


class ProcessorList(generics.ListCreateAPIView):
    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer


class ProcessorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer


class MotherBoardList(generics.ListCreateAPIView):
    queryset = MotherBoard.objects.all()
    serializer_class = MotherBoardSerializer


class MotherBoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MotherBoard.objects.all()
    serializer_class = MotherBoardSerializer


class MemoryList(generics.ListCreateAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer


class MemoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer


class GraphicCardList(generics.ListCreateAPIView):
    queryset = GraphicCard.objects.all()
    serializer_class = GraphicCardSerializer


class GraphicCardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GraphicCard.objects.all()
    serializer_class = GraphicCardSerializer


class ComputerList(generics.ListCreateAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer


class ComputerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
