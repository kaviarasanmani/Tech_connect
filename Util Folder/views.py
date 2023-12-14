# from rest_framework import generics
# from .models import iPhone14
# from .serializers import iPhone14Serializer

# class iPhone14List(generics.ListCreateAPIView):
#     queryset = iPhone14.objects.all()
#     serializer_class = iPhone14Serializer

# class iPhone14Detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = iPhone14.objects.all()
#     serializer_class = iPhone14Serializer

from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        color = self.request.query_params.get('color')
        storage = self.request.query_params.get('storage')
        if color or storage:
            queryset = queryset.filter(variants__color=color, variants__storage=storage).distinct()
        return queryset
