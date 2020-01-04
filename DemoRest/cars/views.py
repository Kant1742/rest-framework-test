from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated, IsAdminUser)
    
from .permissions import IsOwnerOrReadOnly
from .models import Car
from .serializers import (CarsListSerializer,
                          CarDetailSerializer)


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarsListView(generics.ListAPIView):
    serializer_class = CarsListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticated, )


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser)
