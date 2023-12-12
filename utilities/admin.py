# # from django.contrib import admin

# # # Register your models here.
# # from .models import *

# # admin.site.register(Product)
# # admin.site.register(ProductImage)
# # admin.site.register(ProductReview)
# # admin.site.register(ProductSpecification)
# # admin.site.register(ProductVariant)


# # # admin.site.register(Category)
# # # admin.site.register(Subcategory)
# # # admin.site.register(Brand)
# # # # admin.site.register(Variant)



# # admin.py

# from django.contrib import admin
# from .models import Category, Brand, Specification, Product, ProductSpecification, ProductImage, ProductReview, ProductVariant


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name',)}


# class BrandAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug', 'description', 'website']
#     prepopulated_fields = {'slug': ('name',)}


# class SpecificationAdmin(admin.ModelAdmin):
#     list_display = ['name', 'unit']


# class ProductSpecificationInline(admin.TabularInline):
#     model = ProductSpecification
#     extra = 1


# class ProductImageInline(admin.TabularInline):
#     model = ProductImage
#     extra = 1


# class ProductReviewInline(admin.TabularInline):
#     model = ProductReview
#     extra = 1


# class ProductVariantInline(admin.TabularInline):
#     model = ProductVariant
#     extra = 1


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'category', 'brand', 'model', 'price', 'availability']
#     list_filter = ['category', 'brand', 'availability']
#     search_fields = ['name', 'model']
#     inlines = [ProductSpecificationInline, ProductImageInline, ProductReviewInline, ProductVariantInline]


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Brand, BrandAdmin)
# admin.site.register(Specification, SpecificationAdmin)
# admin.site.register(Product, ProductAdmin)


from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Category, Brand, Specification, Product, ProductSpecification, ProductImage, ProductReview, ProductVariant,RecentStory


class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class BrandAdmin(ImportExportModelAdmin):
    list_display = ['name', 'slug', 'description', 'website']
    prepopulated_fields = {'slug': ('name',)}


class SpecificationAdmin(ImportExportModelAdmin):
    list_display = ['name', 'unit']


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification
    extra = 1


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductReviewInline(admin.TabularInline):
    model = ProductReview
    extra = 1


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1


class ProductAdmin(ImportExportModelAdmin):
    list_display = ['name', 'category', 'brand', 'model', 'price', 'availability']
    list_filter = ['category', 'brand', 'availability']
    search_fields = ['name', 'model']
    inlines = [ProductSpecificationInline, ProductImageInline, ProductReviewInline, ProductVariantInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Specification, SpecificationAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(RecentStory)

