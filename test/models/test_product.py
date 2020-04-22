from unittest import TestCase

from code.models.product import Product


class TestProduct(TestCase):

    def test_should_return_price(self):
        product = Product("product", 10)
        assert product.get_price() == 10

    def test_should_return_name(self):
        product = Product("product", 10)
        assert product.get_name() == "product"
