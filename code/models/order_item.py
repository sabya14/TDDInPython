class OrderItem:
    def __init__(self, product, quantity):
        self._product = product
        self._quantity = quantity

    def get_price(self):
        return self._product.get_price() * self._quantity

    def get_discounted_price(self):
        if self._quantity > 10:
            return self.get_price() * 0.9
        else:
            return self.get_price()
