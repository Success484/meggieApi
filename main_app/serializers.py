from rest_framework import serializers
from .models import ClothingItem, Category, ClothingClass

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ClothingClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingClass
        fields = ['id', 'name']

class ClothingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingItem
        fields = ['id', 'image', 'price', 'name', 'clothing_class', 'previous_amount', 'discount', 'category', 'description']
