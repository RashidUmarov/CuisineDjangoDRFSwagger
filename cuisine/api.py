import django_filters.rest_framework

from .models import *
from rest_framework import viewsets, permissions
from .serializers import CategorySerializer, DishSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """Список категорий"""
    queryset = Category.objects.all()
    permission_classes = [
        permissions.AllowAny
        # permissions.IsAuthenticatedOrReadOnly
    ]

    serializer_class = CategorySerializer


class DishViewSet(viewsets.ModelViewSet):
    """Список блюд"""
    queryset = Dish.objects.all()
    permission_classes = [
        permissions.AllowAny
        # permissions.IsAuthenticatedOrReadOnly
    ]

    serializer_class = DishSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['category']
