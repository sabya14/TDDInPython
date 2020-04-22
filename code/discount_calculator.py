def calculate_discount(purchases_count):
    if purchases_count > 30:
        return 30
    elif purchases_count > 20:
        return 20
    elif purchases_count > 10:
        return 10
    else:
        return 0


def get_product_price(product_price, previous_purchase):
    discount = calculate_discount(previous_purchase)
    return (100 - discount) /100 * product_price


def driver():
    price = get_product_price(100, previous_purchase=50)
    print(price)


if __name__ == "__main__":
    driver()