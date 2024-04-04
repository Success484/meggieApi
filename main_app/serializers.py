from rest_framework import serializers
from .models import ClothingItem, Category, ClothingClass, Store

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'text', 'image', 'clothing_class']

class ClothingClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingClass
        fields = ['id', 'name']

class ClothingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingItem
        fields = ['id', 'image', 'price', 'name', 'clothing_class', 'previous_amount', 'discount', 'category', 'description']


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name']