from unittest import TestCase
from unittest.mock import patch

from code.models.product import Product
from code.models.user import User
from code.services.order import Order


class TestOrder(TestCase):

    @patch("code.models.user.User")
    @patch("code.models.order_item.OrderItem")
    def test_order_gives_10_percent_discount_when_previous_purchase_of_same_product_is_more_than_10(self,
                                                                                                    mock_order_item,
                                                                                                    mock_user):

        mock_order_item.get_price.return_value = 100
        order = Order(mock_user, [mock_order_item, mock_order_item])
        assert order.get_order_price() == 200
