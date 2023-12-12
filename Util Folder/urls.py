from django.urls import path
from . import views

urlpatterns = [
    path('iphone14/', views.iPhone14List.as_view(), name='iphone14-list'),
    path('iphone14/<int:pk>/', views.iPhone14Detail.as_view(), name='iphone14-detail'),
]
