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


# # # views.py

# # from rest_framework import viewsets
# # from .models import Category, Brand, Specification, Product, ProductSpecification, ProductImage, ProductReview, ProductVariant
# # from .serializer import CategorySerializer, BrandSerializer, SpecificationSerializer, ProductSerializer, \
# #     ProductSpecificationSerializer, ProductImageSerializer, ProductReviewSerializer, ProductVariantSerializer


# # class CategoryViewSet(viewsets.ModelViewSet):
# #     queryset = Category.objects.all()
# #     serializer_class = CategorySerializer


# # class BrandViewSet(viewsets.ModelViewSet):
# #     queryset = Brand.objects.all()
# #     serializer_class = BrandSerializer


# # class SpecificationViewSet(viewsets.ModelViewSet):
# #     queryset = Specification.objects.all()
# #     serializer_class = SpecificationSerializer


# # class ProductViewSet(viewsets.ModelViewSet):
# #     queryset = Product.objects.all()
# #     serializer_class = ProductSerializer


# # class ProductSpecificationViewSet(viewsets.ModelViewSet):
# #     queryset = ProductSpecification.objects.all()
# #     serializer_class = ProductSpecificationSerializer


# # class ProductImageViewSet(viewsets.ModelViewSet):
# #     queryset = ProductImage.objects.all()
# #     serializer_class = ProductImageSerializer


# # class ProductReviewViewSet(viewsets.ModelViewSet):
# #     queryset = ProductReview.objects.all()
# #     serializer_class = ProductReviewSerializer


# # class ProductVariantViewSet(viewsets.ModelViewSet   ):
# #     queryset = ProductVariant.objects.all()
# #     serializer_class = ProductVariantSerializer



# # views.py

# from rest_framework import viewsets
# from .models import Category, Brand, Specification, Product, ProductSpecification, ProductImage, ProductReview, ProductVariant, RecentStory
# from .serializer import CategorySerializer, BrandSerializer, SpecificationSerializer, ProductSerializer, \
#     ProductSpecificationSerializer, ProductImageSerializer, ProductReviewSerializer, ProductVariantSerializer, RecentStorySerializer


# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class BrandViewSet(viewsets.ModelViewSet):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer


# class SpecificationViewSet(viewsets.ModelViewSet):
#     queryset = Specification.objects.all()
#     serializer_class = SpecificationSerializer


# class ProductSpecificationViewSet(viewsets.ModelViewSet):
#     queryset = ProductSpecification.objects.all()
#     serializer_class = ProductSpecificationSerializer


# class ProductImageViewSet(viewsets.ModelViewSet):
#     queryset = ProductImage.objects.all()
#     serializer_class = ProductImageSerializer


# class ProductReviewViewSet(viewsets.ModelViewSet):
#     queryset = ProductReview.objects.all()
#     serializer_class = ProductReviewSerializer


# class ProductVariantViewSet(viewsets.ModelViewSet):
#     queryset = ProductVariant.objects.all()
#     serializer_class = ProductVariantSerializer


# class RecentStoryViewSet(viewsets.ModelViewSet):
#     queryset = RecentStory.objects.all()
#     serializer_class = RecentStorySerializer


# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filterset_fields = ['category', 'brand']  # You can add more fields for filtering if needed

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         if 'recent_story' in self.request.query_params:
#             # If the 'recent_story' parameter is provided in the query, include recent story data
#             queryset = queryset.prefetch_related('recentstory')
#         return queryset


# views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Category, Brand, Specification, Product, ProductSpecification, ProductImage, ProductReview, ProductVariant, RecentStory
from .serializer import CategorySerializer, BrandSerializer, SpecificationSerializer, ProductSerializer, \
    ProductSpecificationSerializer, ProductImageSerializer, ProductReviewSerializer, ProductVariantSerializer, RecentStorySerializer


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
    filterset_fields = ['category', 'brand']  # You can add more fields for filtering if needed

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        # Manually serialize recent story data for each product
        for data in serializer.data:
            product_id = data['id']
            recent_story = RecentStory.objects.filter(product_id=product_id).first()

            if recent_story:
                recent_story_serializer = RecentStorySerializer(recent_story)
                data['recent_story'] = recent_story_serializer.data
            else:
                data['recent_story'] = None

        return Response(serializer.data, status=status.HTTP_200_OK)

