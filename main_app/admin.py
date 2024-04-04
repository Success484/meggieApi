from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(ClothingClass)
admin.site.register(ClothingItem)
admin.site.register(Store)