from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BrandViewSet, SpecificationViewSet, ProductViewSet, \
    ProductSpecificationViewSet, ProductImageViewSet, ProductReviewViewSet, ProductVariantViewSet, RecentStoryViewSet ,ProductVariantDetailView

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
    path('product-variant/<int:id>/', ProductVariantDetailView.as_view(), name='product-variant-detail'),
]

