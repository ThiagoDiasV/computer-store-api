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
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin


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


class Index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "index.html"

    def get(self, request):
        queryset = Processor.objects.all()

        # from ipdb import set_trace; set_trace()
        return Response({"orders": queryset})
