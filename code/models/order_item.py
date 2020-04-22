class OrderItem:
    def __init__(self, product, quantity):
        self._product = product
        self._quantity = quantity

    def get_price(self):
        return self._product.get_price() * self._quantity
