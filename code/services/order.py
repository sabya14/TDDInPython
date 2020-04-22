class Order:
    def __init__(self, user, products):
        self.user = user
        self.products = products
        self.total_price = 0

    def get_order_price(self):
        for product in self.products:
            price = product.get_price()
            self.total_price += price
