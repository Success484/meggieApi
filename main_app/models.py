from django.db import models

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ClothingClass(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ClothingItem(models.Model):
    image = models.ImageField(upload_to='clothing_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)
    clothing_class = models.ForeignKey(ClothingClass, on_delete=models.CASCADE)
    previous_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name
