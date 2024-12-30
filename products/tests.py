# from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Product
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse


# Create your tests here.
# * model testing
class ProductTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="test-user", password="123456")
        cls.product = Product.objects.create(
            title="title",
            description="test description",
            price=20.25,
            owner=cls.user,
            available=False,
        )
        cls.data = {
            "title": "test",
            "description": "test",
            "price": 100,
            "owner": cls.user.id,
            "available": False,
        }

    def setUp(self):
        self.client.login(username="test-user", password="123456")

    def test_user_content(self):
        self.assertEqual(self.user.username, "test-user")

    def test_Product_content(self):
        self.assertEqual(self.product.title, "title")
        self.assertEqual(self.product.description, "test description")
        self.assertEqual(self.product.price, 20.25)
        self.assertEqual(self.product.owner, self.user)
        self.assertEqual(self.product.available, False)

    def test_list_view(self):
        response = self.client.get(reverse("product_list_create"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.count(), 1)
        self.assertContains(response, self.product)

    def test_create_view(self):
        response = self.client.post(reverse("product_list_create"), data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(Product.objects.first().title, "title")
        self.assertEqual(Product.objects.last().title, "test")
        self.assertEqual(response.json()["title"], "test")
