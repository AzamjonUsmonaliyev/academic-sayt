from django.shortcuts import render
from .models import Category,Product
from .serializers import CategorySerializer ,ProductSerializer
from rest_framework.viewsets import ModelViewSet

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer