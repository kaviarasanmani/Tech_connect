# # from rest_framework import serializers
# # from .models import Category, Brand, Specification, Product, ProductSpecification, ProductImage, ProductReview, ProductVariant


# # class CategorySerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Category
# #         fields = '__all__'


# # class BrandSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Brand
# #         fields = '__all__'


# # class SpecificationSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Specification
# #         fields = '__all__'


# # class ProductSpecificationSerializer(serializers.ModelSerializer):
# #     specification = SpecificationSerializer()

# #     class Meta:
# #         model = ProductSpecification
# #         fields = ['specification', 'value']


# # class ProductImageSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = ProductImage
# #         fields = ['image']


# # class ProductReviewSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = ProductReview
# #         fields = '__all__'


# # class ProductVariantSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = ProductVariant
# #         fields = '__all__'


# # class ProductSerializer(serializers.ModelSerializer):
# #     category = CategorySerializer()
# #     brand = BrandSerializer()
# #     specifications = ProductSpecificationSerializer(many=True, source='productspecification_set')
# #     images = ProductImageSerializer(many=True, source='productimage_set')
# #     reviews = ProductReviewSerializer(many=True, source='productreview_set')
# #     variants = ProductVariantSerializer(many=True, source='productvariant_set')

# #     class Meta:
# #         model = Product
# #         fields = '__all__'


# # serializers.py

# from rest_framework import serializers
# from .models import Category, Brand, Specification, Product, ProductSpecification, ProductImage, ProductReview, ProductVariant,RecentStory


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'


# class BrandSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Brand
#         fields = '__all__'


# class SpecificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Specification
#         fields = '__all__'


# class ProductSpecificationSerializer(serializers.ModelSerializer):
#     specification = SpecificationSerializer()

#     class Meta:
#         model = ProductSpecification
#         fields = ['specification', 'value']


# class ProductImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductImage
#         fields = ['image']


# class ProductReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductReview
#         fields = '__all__'


# class ProductVariantSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductVariant
#         fields = '__all__'


# # class ProductStory(serializers.ModelSerializer):

# class ProductStorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecentStory
#         fields = ['title',
#                   'content',
#                   'author',
#                   'pub_date',
#                   ]


# class ProductSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()
#     brand = BrandSerializer()
#     specifications = ProductSpecificationSerializer(many=True, source='productspecification_set')
#     images = ProductImageSerializer(many=True, source='productimage_set')
#     reviews = ProductReviewSerializer(many=True, source='productreview_set')
#     variants = ProductVariantSerializer(many=True, source='productvariant_set')
#     recent_story = ProductStorySerializer()

#     class Meta:
#         model = Product
#         fields = '__all__'


# serializers.py

from rest_framework import serializers
from .models import Category, Brand, Specification, Product, ProductSpecification, ProductImage, ProductReview, ProductVariant, RecentStory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = '__all__'


class ProductSpecificationSerializer(serializers.ModelSerializer):
    specification = SpecificationSerializer()

    class Meta:
        model = ProductSpecification
        fields = ['specification', 'value']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = '__all__'


class RecentStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentStory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()
    specifications = ProductSpecificationSerializer(many=True, source='productspecification_set')
    images = ProductImageSerializer(many=True, source='productimage_set')
    reviews = ProductReviewSerializer(many=True, source='productreview_set')
    variants = ProductVariantSerializer(many=True, source='productvariant_set')
    recent_story = RecentStorySerializer(many=True,source='recentstory', read_only=True)  # Linking recent story

    class Meta:
        model = Product
        fields = '__all__'

