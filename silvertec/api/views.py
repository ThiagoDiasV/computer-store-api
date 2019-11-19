from .models import Processor, MotherBoard
from .serializers import ProcessorSerializer, MotherBoardSerializer
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
