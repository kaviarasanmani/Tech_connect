from django.urls import path
from .views import SearchAPIView, ProductAPIView

urlpatterns = [
    path('search/', SearchAPIView.as_view(), name='search_api'),
    path('product/', ProductAPIView.as_view(), name='product_api'),
]
