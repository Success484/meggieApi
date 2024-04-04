from rest_framework import generics
from .models import Category, ClothingClass, ClothingItem, Store
from .serializers import CategorySerializer, ClothingClassSerializer, ClothingItemSerializer, StoreSerializer


# Category
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Store
class StoreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class StoreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


# Clothing_class
class ClothingClassListCreateAPIView(generics.ListCreateAPIView):
    queryset = ClothingClass.objects.all()
    serializer_class = ClothingClassSerializer

class ClothingClassRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClothingClass.objects.all()
    serializer_class = ClothingClassSerializer


# Clothings
class ClothingItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = ClothingItem.objects.all()
    serializer_class = ClothingItemSerializer

class ClothingItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClothingItem.objects.all()
    serializer_class = ClothingItemSerializer
