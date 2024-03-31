from rest_framework import generics
from .models import Category, ClothingClass, ClothingItem
from .serializers import CategorySerializer, ClothingClassSerializer, ClothingItemSerializer

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ClothingClassListCreateAPIView(generics.ListCreateAPIView):
    queryset = ClothingClass.objects.all()
    serializer_class = ClothingClassSerializer

class ClothingClassRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClothingClass.objects.all()
    serializer_class = ClothingClassSerializer

class ClothingItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = ClothingItem.objects.all()
    serializer_class = ClothingItemSerializer

class ClothingItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClothingItem.objects.all()
    serializer_class = ClothingItemSerializer
