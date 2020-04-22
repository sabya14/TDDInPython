class Order:
    def __init__(self, user, order_items):
        self.user = user
        self.order_items = order_items
        self.total_price = 0

    def get_order_price(self):
        for order_items in self.order_items:
            price = order_items.get_price()
            self.total_price += price
        return self.total_price
