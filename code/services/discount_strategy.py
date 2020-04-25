import abc
from math import floor


class DiscountStrategy(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def get_discounted_price(present_price): pass


class PercentageDiscount(DiscountStrategy):

    def __init__(self, order_item, discount_percentage):
        self.order_item = order_item
        self.discount_percentage = discount_percentage

    def get_discounted_price(self, present_price):
        if self.discount_percentage and self.order_item.get_quantity() > 10:
            return present_price * (1 - self.discount_percentage / 100)
        return present_price


class SpecialUserDiscount(DiscountStrategy):

    def __init__(self, order_item, discount_info):
        self.order_item = order_item
        self.discount_info = discount_info

    def get_discounted_price(self, present_price):
        try:
            user_type = self.order_item.get_user_type()
            discount_percentage = self.discount_info[user_type]
            return present_price * (1 - discount_percentage / 100)
        except KeyError:
            return present_price


class BoughtTogetherDiscount(DiscountStrategy):

    def __init__(self, order_item, discount_info):
        self.order_item = order_item
        self.discount_info = discount_info

    def get_discounted_price(self, present_price):
        minimum_quantity_get_free = self.discount_info[0]
        present_price -= floor(
            self.order_item.get_quantity() / minimum_quantity_get_free) * self.order_item.get_product_price()
        return present_price
