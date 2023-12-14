# from rest_framework import serializers
# from .models import Category, Brand, Specification, Product, ProductSpecification, ProductImage, ProductReview, ProductVariant, RecentStory,Videos


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


# class RecentStorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecentStory
#         fields = '__all__'

# class VideosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Videos
#         fields = '__all__'

# class ProductSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()
#     brand = BrandSerializer()
#     specifications = ProductSpecificationSerializer(many=True, source='productspecification_set')
#     images = ProductImageSerializer(many=True, source='productimage_set')
#     reviews = ProductReviewSerializer(many=True, source='productreview_set')
#     variants = ProductVariantSerializer(many=True, source='productvariant_set')
#     recent_story = RecentStorySerializer(many=True,source='recentstory', read_only=True)  
#     videos = VideosSerializer(many=True,source='url',read_only=True)
#     # Linking recent story

#     class Meta:
#         model = Product
#         fields = '__all__'

from rest_framework import serializers
from .models import Category, Brand, Specification, Product, ProductSpecification, ProductImage, ProductReview, ProductVariant, RecentStory, Videos, Competitor


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


class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'


class CompetitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competitor
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()
    specifications = ProductSpecificationSerializer(many=True, source='productspecification_set')
    images = ProductImageSerializer(many=True, source='productimage_set')
    reviews = ProductReviewSerializer(many=True, source='productreview_set')
    variants = ProductVariantSerializer(many=True, source='productvariant_set')
    recent_story = RecentStorySerializer(many=True, source='recentstory_set', read_only=True)
    videos = VideosSerializer(many=True, source='videos_set', read_only=True)
    competitor = CompetitorSerializer(many=True, source='competitor_set', read_only=True)


    class Meta:
        model = Product
        fields = '__all__'




