from django.urls import path
from .views import CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView, ClothingClassListCreateAPIView, ClothingClassRetrieveUpdateDestroyAPIView, ClothingItemListCreateAPIView, ClothingItemRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
    path('clothing-classes/', ClothingClassListCreateAPIView.as_view(), name='clothing-class-list-create'),
    path('clothing-classes/<int:pk>/', ClothingClassRetrieveUpdateDestroyAPIView.as_view(), name='clothing-class-detail'),
    path('clothing/', ClothingItemListCreateAPIView.as_view(), name='clothing-list-create'),
    path('clothing/<int:pk>/', ClothingItemRetrieveUpdateDestroyAPIView.as_view(), name='clothing-detail'),
]
