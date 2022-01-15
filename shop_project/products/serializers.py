from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'seller', 'name', 'price')
        model = Product