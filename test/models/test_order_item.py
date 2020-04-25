from unittest import TestCase
from unittest.mock import patch, Mock

from code.configs.discount_types import DiscountTypes
from code.models.order_item import OrderItem


class TestOrderItem(TestCase):

    @patch("code.models.product.Product")
    def test_a_order_item_should_return_price(self, product_mock):
        product_mock.get_name.return_value = 'test-val-1'
        product_mock.get_price.return_value = 10
        item = OrderItem(product_mock, 10)
        assert item.get_price() == 100

    @patch("code.models.product.Product")
    def test_a_order_item_should_return_give_10_percent_discount_if_quantity_more_than_10(self, product_mock):
        product_mock.get_name.return_value = 'test-val-1'
        product_mock.get_price.return_value = 10
        item_10_quantity = OrderItem(product_mock, 10)
        discounts = [{"type": DiscountTypes.Percentage.value, "value": 10}]

        assert item_10_quantity.get_discounted_price(discounts) != 90

        item_11_quantity = OrderItem(product_mock, 11)
        assert item_11_quantity.get_discounted_price(discounts) == 99

    @patch("code.models.product.Product")
    def test_a_order_item_should_gives_extra_10_percent_when_user_type_special(self, product_mock):
        product_mock.get_name.return_value = 'test-val-1'
        product_mock.get_price.return_value = 10
        item_20_quantity = OrderItem(product_mock, 10, "special")
        discounts = [{"type": DiscountTypes.User.value, "value": {"special": 10}}]
        assert item_20_quantity.get_discounted_price(discounts) == 90

    @patch("code.models.product.Product")
    def test_when_3_product_are_bought_price_is_of_two(self, product_mock):
        product_mock.get_name.return_value = 'test-val-1'
        product_mock.get_price.return_value = 10
        item_20_quantity = OrderItem(product_mock, 3)
        discounts = [{"type": "bought_together", "value": (3, 2)}]
        assert item_20_quantity.get_discounted_price(discounts) == 20

    @patch("code.models.product.Product")
    def test_whether_10_percent_special_3at2_work_together(self, product_mock):
        product_mock.get_name.return_value = 'test-val-1'
        product_mock.get_price.return_value = 10
        item_20_quantity = OrderItem(product_mock, 20, "special")
        discounts = [{"type": "percent", "value": 10}, {"type": DiscountTypes.User.value, "value": {"special": 5}},
                     {"type": "bought_together", "value": (3, 2)}]
        print(item_20_quantity.get_discounted_price(discounts))
        assert item_20_quantity.get_discounted_price(discounts) == 111.0
