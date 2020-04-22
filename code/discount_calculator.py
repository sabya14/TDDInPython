def calculate_discount(purchases_count):
    if purchases_count > 10:
        return 10
    else:
        return 0


def get_product_price(product_price):
    previous_purchase = 50
    discount = calculate_discount(previous_purchase)
    return (100 - discount)/100 * product_price


def driver():
    price = get_product_price(100)
    print(price)


if __name__ == "__main__":
    driver()