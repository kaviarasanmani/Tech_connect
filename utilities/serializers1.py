# # serializers.py
# from rest_framework import serializers
# from .models import ProductVariant, Product, ProductSpecification, ProductImage, ProductReview, RecentStory, Competitor

# class ProductSpecificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductSpecification
#         fields = '__all__'

# class ProductImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductImage
#         fields = '__all__'

# class ProductReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductReview
#         fields = '__all__'

# class RecentStorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecentStory
#         fields = '__all__'

# class CompetitorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Competitor
#         fields = '__all__'

# # class ProductSerializer(serializers.ModelSerializer):
# #     specifications = ProductSpecificationSerializer(many=True, read_only=True)
# #     images = ProductImageSerializer(many=True, read_only=True)
# #     reviews = ProductReviewSerializer(many=True, read_only=True)
# #     recent_stories = RecentStorySerializer(many=True, read_only=True)
# #     competitors = CompetitorSerializer(many=True, read_only=True)

# #     class Meta:
# #         model = Product
# #         fields = '__all__'

# # class ProductVariantSerializer_id(serializers.ModelSerializer):
# #     product = ProductSerializer()

# #     class Meta:
# #         model = ProductVariant
# #         fields = '__all__'


# class ProductSerializer(serializers.ModelSerializer):
#     specifications = ProductSpecificationSerializer(many=True, read_only=True)
#     images = ProductImageSerializer(many=True, read_only=True)
#     reviews = ProductReviewSerializer(many=True, read_only=True)
#     recent_stories = RecentStorySerializer(many=True, read_only=True)
#     competitors = CompetitorSerializer(many=True, read_only=True)

#     class Meta:
#         model = Product
#         fields = '__all__'

# class ProductVariantSerializer_id(serializers.ModelSerializer):
#     product = ProductSerializer()

#     class Meta:
#         model = ProductVariant
#         fields = '__all__'

from rest_framework import serializers
from .models import *

class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = '__all__'

class ProductSpecificationSerializer(serializers.ModelSerializer):
    specification = SpecificationSerializer()

    class Meta:
        model = ProductSpecification
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
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
class ProductSerializer1(serializers.ModelSerializer):
    specifications = ProductSpecificationSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    reviews = ProductReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'



class ProductVariantSerializer_id(serializers.ModelSerializer):
    product = ProductSerializer1()
    specifications = ProductSpecificationSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    reviews = ProductReviewSerializer(many=True, read_only=True)

    class Meta:
        model = ProductVariant
        fields = '__all__'
