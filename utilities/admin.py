# from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
# from .models import Category, Brand, Specification, Product, ProductSpecification, ProductImage, ProductReview, ProductVariant,RecentStory,Videos,Competitor


# class CategoryAdmin(ImportExportModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name',)}


# class BrandAdmin(ImportExportModelAdmin):
#     list_display = ['name', 'slug', 'description', 'website']
#     prepopulated_fields = {'slug': ('name',)}


# class SpecificationAdmin(ImportExportModelAdmin):
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


# class ProductAdmin(ImportExportModelAdmin):
#     list_display = ['name', 'category', 'brand', 'model', 'price', 'availability']
#     list_filter = ['category', 'brand', 'availability']
#     search_fields = ['name', 'model']
#     inlines = [ProductSpecificationInline, ProductImageInline, ProductReviewInline, ProductVariantInline]


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Brand, BrandAdmin)
# admin.site.register(Specification, SpecificationAdmin)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(RecentStory)
# admin.site.register(Videos)
# admin.site.register(Competitor)



from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Category, Brand, Specification, Product, ProductSpecification, ProductImage, ProductReview, ProductVariant, RecentStory, Videos, Competitor


class BaseModelAdmin(ImportExportModelAdmin):
    pass


class CategoryAdmin(BaseModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Brand)
class BrandAdmin(BaseModelAdmin):
    list_display = ['name', 'slug', 'description', 'website']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Specification)
class SpecificationAdmin(BaseModelAdmin):
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


class RecentStoryInline(admin.TabularInline):
    model = RecentStory
    extra = 1


class VideosInline(admin.TabularInline):
    model = Videos
    extra = 1


class CompetitorInline(admin.TabularInline):
    model = Competitor
    extra = 1


@admin.register(Product)
class ProductAdmin(BaseModelAdmin):
    list_display = ['name', 'category', 'brand', 'model', 'price', 'availability']
    list_filter = ['category', 'brand', 'availability']
    search_fields = ['name', 'model']
    inlines = [ProductSpecificationInline, ProductImageInline, ProductReviewInline, ProductVariantInline, RecentStoryInline, VideosInline, CompetitorInline]


@admin.register(RecentStory)
class RecentStoryAdmin(BaseModelAdmin):
    pass


@admin.register(Videos)
class VideosAdmin(BaseModelAdmin):
    pass


@admin.register(Competitor)
class CompetitorAdmin(BaseModelAdmin):
    pass

