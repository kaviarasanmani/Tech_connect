# # # from rest_framework.views import APIView
# # # from rest_framework.response import Response
# # # import requests
# # # import os
# # # import json

# # # api_key = 'hZbZngFDeHnjG51ajU9XB6WH'


# # # class SearchAPIView(APIView):
# # #     def get(self, request):
# # #         query = request.GET.get('q', '')
# # #         api_url = "https://www.searchapi.io/api/v1/search"
# # #         params = {
# # #             "engine": "google_shopping",
# # #             "q": query,
# # #             "location": "Tamil Nadu,India",
# # #             "location_used": "Tamil Nadu,India",
# # #             "google_domain": "google.co.in",
# # #             "hl": "en",
# # #             "gl": "in",
# # #             "num": "60",
# # #             "api_key": api_key
# # #         }

# # #         response = requests.get(api_url, params=params)
# # #         if response.status_code == 200:
# # #             data = response.json()
# # #             return Response(data)
# # #         else:
# # #             return Response({"error": f"Error: {response.status_code}, {response.text}"})


# # # class ProductAPIView(APIView):
# # #     def get(self, request):
# # #         product_id = request.GET.get('q', '')
# # #         api_url = "https://www.searchapi.io/api/v1/search"

# # #         params = {
# # #             "engine": "google_product",
# # #             "product_id": product_id,
# # #             "api_key": api_key,
# # #             "google_domain": "google.co.in",
# # #             "gl": "in",

# # #         }
# # #         response = requests.get(api_url, params=params)
# # #         if response.status_code == 200:
# # #             data = response.json()
# # #             return Response(data)
# # #         else:
# # #             return Response({"error": f"Error: {response.status_code}, {response.text}"})


# # # class TrendingAPIView(APIView):
# # #     def get(self, request):
# # #         q = request.GET.get('q', '')
# # #         api_url = "https://www.searchapi.io/api/v1/search"

# # #         params = {
# # #             "engine": "google",
# # #             "q": q,
# # #             "api_key": api_key,
# # #             "google_domain": "google.co.in",
# # #             "gl": "in",

# # #         }
# # #         response = requests.get(api_url, params=params)
# # #         if response.status_code == 200:
# # #             data = response.json()
# # #             return Response(data)
# # #         else:
# # #             return Response({"error": f"Error: {response.status_code}, {response.text}"})


from rest_framework import viewsets, status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Brand, Specification, Product, ProductSpecification, ProductImage, ProductReview, ProductVariant, RecentStory
from .serializer import CategorySerializer, BrandSerializer, SpecificationSerializer, ProductSerializer, \
    ProductSpecificationSerializer, ProductImageSerializer, ProductReviewSerializer, ProductVariantSerializer, RecentStorySerializer
from .serializers1 import ProductVariantSerializer_id

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class SpecificationViewSet(viewsets.ModelViewSet):
    queryset = Specification.objects.all()
    serializer_class = SpecificationSerializer


class ProductSpecificationViewSet(viewsets.ModelViewSet):
    queryset = ProductSpecification.objects.all()
    serializer_class = ProductSpecificationSerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer


class ProductVariantViewSet(viewsets.ModelViewSet):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer


class RecentStoryViewSet(viewsets.ModelViewSet):
    queryset = RecentStory.objects.all()
    serializer_class = RecentStorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # You can add more fields for filtering if needed
    filterset_fields = ['category', 'brand']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        # Manually serialize recent story data for each product
        for data in serializer.data:
            product_id = data['id']
            recent_story = RecentStory.objects.filter(
                product_id=product_id).first()

            if recent_story:
                recent_story_serializer = RecentStorySerializer(recent_story)
                data['recent_story'] = recent_story_serializer.data
            else:
                data['recent_story'] = None

        return Response(serializer.data, status=status.HTTP_200_OK)




class ProductVariantDetailView(APIView):
    def get(self, request, id):
        try:
            product_variant = ProductVariant.objects.get(id=id)
        except ProductVariant.DoesNotExist:
            return Response({"detail": "ProductVariant not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductVariantSerializer_id(product_variant)
        return Response(serializer.data, status=status.HTTP_200_OK)