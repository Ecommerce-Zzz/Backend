from django.test import TestCase
from .models import Product
from django.contrib.auth.models import User


# Create your tests here.
# * model testing
class ProductTests(TestCase):
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

    def test_user_content(self):
        self.assertEqual(self.user.username, "test-user")

    def test_Product_content(self):
        self.assertEqual(self.product.title, "title")
        self.assertEqual(self.product.description, "test description")
        self.assertEqual(self.product.price, 20.25)
        self.assertEqual(self.product.owner, self.user)
        self.assertEqual(self.product.available, False)
