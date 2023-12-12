from rest_framework import serializers
from .models import (
    Manufacturer, Offer, Feature, SpecificationAttribute, Specification,
    Review, ProductReview, EditorialReview, iPhone14
)

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'

class SpecificationAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificationAttribute
        fields = '__all__'

class SpecificationSerializer(serializers.ModelSerializer):
    attributes = SpecificationAttributeSerializer(many=True)

    class Meta:
        model = Specification
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'

class EditorialReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditorialReview
        fields = '__all__'

class iPhone14Serializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()
    offers = OfferSerializer(many=True)
    features = FeatureSerializer(many=True)
    specifications = SpecificationSerializer(many=True)
    web_reviews = ReviewSerializer(many=True, source='web_reviews')
    product_reviews = ProductReviewSerializer(many=True)
    editorial_reviews = EditorialReviewSerializer(many=True)
    images = serializers.JSONField()

    class Meta:
        model = iPhone14
        fields = '__all__'
