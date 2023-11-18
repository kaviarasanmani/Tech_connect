from django.urls import path
from .views import SearchAPIView
# de

urlpatterns = [
    path('search/', SearchAPIView.as_view(), name='search_api'),
]
