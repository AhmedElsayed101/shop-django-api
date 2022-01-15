from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import Client, TestCase
from django.urls import reverse


from .models import Product

class BookTests(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username = 'test',
            email = 'test@email.com',
            password = 'test'
        )

        self.product = Product.objects.create(
            name='product1',
            price=10,
            seller = self.user
        )

    
    def test_name_product(self):
        
        product = Product.objects.get(id=1)
        expected_name = product.name
        self.assertEquals(expected_name, 'product1')

    
    def test_name_product(self):
        
        product = Product.objects.get(id=1)
        expected_price = product.price
        self.assertEquals(expected_price, 10)

    