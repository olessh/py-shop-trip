import math
from datetime import datetime
from app.customer import Customer
from app.shop import Shop


def calculate_distance(location1: list, location2: list) -> float:
    x1, y1 = location1
    x2, y2 = location2

    dx = x2 - x1
    dy = y2 - y1

    return math.sqrt(dx ** 2 + dy ** 2)


def calculate_product_cost(product_cart: dict, shop_products: dict) -> float:
    total_cost = 0
    for product, quantity in product_cart.items():
        if product in shop_products:
            total_cost += quantity * shop_products[product]
    return total_cost


def purchase_and_print_receipt(customer: Customer, shop: Shop) -> None:
    locked_datetime = datetime(2021, 4, 1, 12, 33, 41)
    formatted_datetime = locked_datetime.strftime("%m/%d/%Y %H:%M:%S")
    print(f"\nDate: {formatted_datetime}")
    print(f"Thanks, {customer.name}, for your purchase!"
          f"\nYou have bought:")

    product_cart = customer.product_cart
    shop_products = shop.products

    for product, quantity in product_cart.items():
        cost_product = quantity * shop_products[product]
        formatted_cost_product = str(cost_product).rstrip("0").rstrip(".")
        print(f"{quantity} {product}s for {formatted_cost_product} dollars")

    total_cost = calculate_product_cost(product_cart, shop_products)
    print(f"Total cost is {total_cost} dollars"
          f"\nSee you again!")