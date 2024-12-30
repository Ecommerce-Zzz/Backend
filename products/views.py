from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from drf_spectacular.utils import extend_schema

# Create your views here.


@extend_schema(tags=["Products"])
class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@extend_schema(tags=["Products"])
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
