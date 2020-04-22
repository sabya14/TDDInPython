class OrderItem:
    def __init__(self, product, quantity, user_type=None):
        self._product = product
        self._quantity = quantity
        self._user_type = user_type

    def get_price(self):
        return self._product.get_price() * self._quantity

    def get_discounted_price(self):
        if self._quantity > 10:
            price = self.get_price() * 0.9
        else:
            price = self.get_price()
        if self._user_type == "special":
            price = price * 0.95
        return price
