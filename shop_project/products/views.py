from rest_framework import generics, permissions

from .models import Product
from .serializers import Product, ProductSerializer
from .permissions import IsAuthorOrReadOnly


class ProductList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        self.queryset = Product.objects.all().order_by('seller', 'price')
        return super().list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):

        seller = str(request.user.id)
        request.data._mutable = True
        request.data['seller'] = seller
        request.data._mutable = False

        return super().post(request, *args, **kwargs)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer