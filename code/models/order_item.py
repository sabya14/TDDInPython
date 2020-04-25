from math import floor

from code.services.discount_factory import DiscountFactory


class OrderItem:
    def __init__(self, product, quantity, user_type=None):
        self._product = product
        self._quantity = quantity
        self._user_type = user_type

    def get_price(self):
        return self._product.get_price() * self._quantity

    def get_product_price(self):
        return self._product.get_price()

    def get_quantity(self):
        return self._quantity

    def get_user_type(self):
        return self._user_type

    def get_discounted_price(self, list_of_discount_type):
        price = self.get_price()
        for discount in list_of_discount_type:
            new_price = DiscountFactory(self, discount).get_factory().get_discounted_price(price)
            print(price, new_price)
            price = new_price
        return price
