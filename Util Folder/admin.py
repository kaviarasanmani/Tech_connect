from django.contrib import admin
from .models import Brand, Category, Product, Variant, GalleryItem

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Variant)
admin.site.register(GalleryItem)
