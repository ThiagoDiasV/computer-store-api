from .models import (
    Processor,
    MotherBoard,
    Memory,
    GraphicCard,
    Computer,
    Order,
    User,
)
from .serializers import (
    ProcessorSerializer,
    MotherBoardSerializer,
    MemorySerializer,
    GraphicCardSerializer,
    ComputerSerializer,
    UserSerializer,
    OrderSerializer,
)
from rest_framework import permissions, viewsets


class ProcessorViewSet(viewsets.ModelViewSet):
    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer
    filter_fields = "__all__"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MotherBoardViewSet(viewsets.ModelViewSet):
    queryset = MotherBoard.objects.all()
    serializer_class = MotherBoardSerializer
    filter_fields = "__all__"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MemoryViewSet(viewsets.ModelViewSet):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer
    filter_fields = "__all__"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GraphicCardViewSet(viewsets.ModelViewSet):
    queryset = GraphicCard.objects.all()
    serializer_class = GraphicCardSerializer
    filter_fields = "__all__"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ComputerViewSet(viewsets.ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
    filter_fields = "__all__"


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_fields = "__all__"


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = "__all__"
