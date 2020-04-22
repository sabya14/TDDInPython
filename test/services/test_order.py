from unittest import TestCase
from unittest.mock import patch
from code.services.order import Order


class TestOrder(TestCase):

    @patch("code.models.user.User")
    @patch("code.models.order_item.OrderItem")
    def test_order_correct_price_for_two_order_items(self,
                                                     mock_order_item,
                                                     mock_user):
        mock_order_item.get_price.return_value = 100
        order = Order(mock_user, [mock_order_item, mock_order_item])
        assert order.get_order_price() == 200

    @patch("code.models.user.User")
    @patch("code.models.order_item.OrderItem")
    def test_order_gives_correct_discounted_price(self,
                                                  mock_order_item,
                                                  mock_user):
        mock_order_item.get_discounted_price.return_value = 100
        order = Order(mock_user, [mock_order_item, mock_order_item])
        assert order.get_discounted_order_price() == 200
