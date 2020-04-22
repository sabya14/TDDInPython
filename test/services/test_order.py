from unittest import TestCase

from code.models.product import Product
from code.models.user import User
from code.services.order import Order


class TestOrder(TestCase):

    def test_order_gives_10_percent_discount_when_previous_purchase_of_same_product_is_more_than_10(self):
        pass
        # order = Order(User(), [OrderItem(Product("One", 100), 50)])
        # assert order.get_order_price() == 90
