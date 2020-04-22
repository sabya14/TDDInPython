class Product:
    def __init__(self, name, price):
        self._price = price
        self._name = name

    def get_price(self):
        return self._price

    def get_name(self):
        return self._name

