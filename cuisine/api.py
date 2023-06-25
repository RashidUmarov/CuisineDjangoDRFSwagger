from .models import *
from rest_framework import viewsets, permissions
from .serializers import CategorySerializer, DishSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [
        permissions.AllowAny
        # permissions.IsAuthenticatedOrReadOnly
    ]

    serializer_class = CategorySerializer


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    permission_classes = [
        permissions.AllowAny
        # permissions.IsAuthenticatedOrReadOnly
    ]

    serializer_class = DishSerializer
