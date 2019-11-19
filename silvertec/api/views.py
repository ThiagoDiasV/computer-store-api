from .models import Processor, MotherBoard, Memory, VideoCard
from .serializers import ProcessorSerializer, MotherBoardSerializer, MemorySerializer, VideoCardSerializer
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


class VideoCardList(generics.ListCreateAPIView):
    queryset = VideoCard.objects.all()
    serializer_class = VideoCardSerializer


class VideoCardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VideoCard.objects.all()
    serializer_class = VideoCardSerializer
