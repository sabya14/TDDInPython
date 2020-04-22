def calculate_discount(purchases_count):
    if purchases_count > 30:
        return 30
    elif purchases_count > 20:
        return 20
    elif purchases_count > 10:
        return 10
    else:
        return 0


class User:
    def __init__(self, name, type):
        self.name = name
        self.type = type


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_product_price(user, product_price, previous_purchase=50):
        discount = calculate_discount(previous_purchase)
        if user.type == "special":
            discount += 10
        return (100 - discount) / 100 * product_price


class Order:
    def __init__(self, products_list):
        self.products_list = products_list

    def process(self):
        # Iterate all products if you find more than two, then give one free?
        # Discount category ? Based on user?

        pass


def driver():
    # User object?
    # id, name, type
    user_normal = User("neel", "normal")
    user_special = User("dhwanil", "special")
    print(get_product_price(user_normal, 100, 50))
    print(get_product_price(user_special, 100, 50))


if __name__ == "__main__":
    driver()
