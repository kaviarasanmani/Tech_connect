# # from django.urls import path
# # from .views import SearchAPIView, ProductAPIView

# # urlpatterns = [
# #     path('search/', SearchAPIView.as_view(), name='search_api'),
# #     path('product/', ProductAPIView.as_view(), name='product_api'),
# # ]


# # urls.py

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import CategoryViewSet, BrandViewSet, SpecificationViewSet, ProductViewSet, \
#     ProductSpecificationViewSet, ProductImageViewSet, ProductReviewViewSet, ProductVariantViewSet

# router = DefaultRouter()
# router.register(r'categories', CategoryViewSet)
# router.register(r'brands', BrandViewSet)
# router.register(r'specifications', SpecificationViewSet)
# router.register(r'products', ProductViewSet)
# router.register(r'product-specifications', ProductSpecificationViewSet)
# router.register(r'product-images', ProductImageViewSet)
# router.register(r'product-reviews', ProductReviewViewSet)
# router.register(r'product-variants', ProductVariantViewSet)

# urlpatterns = [
#     path('', include(router.urls)),

# ]



# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BrandViewSet, SpecificationViewSet, ProductViewSet, \
    ProductSpecificationViewSet, ProductImageViewSet, ProductReviewViewSet, ProductVariantViewSet, RecentStoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'specifications', SpecificationViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-specifications', ProductSpecificationViewSet)
router.register(r'product-images', ProductImageViewSet)
router.register(r'product-reviews', ProductReviewViewSet)
router.register(r'product-variants', ProductVariantViewSet)
router.register(r'recent-stories', RecentStoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
