from django.shortcuts import render
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoModelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters


class ProductoViewSet(viewsets.ModelViewSet):

    queryset = Producto.objects.all()
    serializer_class = ProductoModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['codigo']