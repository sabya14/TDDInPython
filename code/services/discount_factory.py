from code.services.discount_strategy import PercentageDiscount, SpecialUserDiscount, BoughtTogetherDiscount


class DiscountFactory:
    def __init__(self, order_item, discount):
        self.order_item = order_item
        self.discount = discount
        self.factories = {
            "percent": PercentageDiscount,
            "user": SpecialUserDiscount,
            "bought_together": BoughtTogetherDiscount
        }

    def get_factory(self):
        return self.factories[self.discount["type"]](self.order_item, self.discount["value"])
