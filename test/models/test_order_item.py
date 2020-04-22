from unittest import TestCase
from unittest import TestCase
from unittest.mock import patch, Mock
from code.models.order_item import OrderItem


class TestOrderItem(TestCase):

    @patch("code.models.product.Product")
    def test_a_order_item_should_return_price(self, product_mock):
        product_mock.get_name.return_value = 'test-val-1'
        product_mock.get_price.return_value = 10
        item = OrderItem(product_mock, 10)
        assert item.get_price() == 100
