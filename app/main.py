import json
from app.customer import Customer
from app.shop import Shop
from app.car import Car
from app.additional_functions import (calculate_distance,
                                      calculate_product_cost,
                                      purchase_and_print_receipt)


def shop_trip() -> None:
    with open("app/config.json") as f:
        config_data = json.load(f)

    customers_data = config_data["customers"]
    shops_data = config_data["shops"]
    fuel_price = config_data["FUEL_PRICE"]

    customers = [Customer(
        customer["name"],
        customer["product_cart"],
        customer["location"],
        customer["money"],
        Car(customer["car"]["brand"],
            customer["car"]["fuel_consumption"])
    )
        for customer in customers_data]
    shops = [Shop(
        shop["name"],
        shop["location"],
        shop["products"]
    )
        for shop in shops_data]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        trip_costs = {}
        for shop in shops:
            distance_to_shop = calculate_distance(
                customer.location,
                shop.location
            )
            fuel_cost_to_shop = fuel_price * \
                distance_to_shop * \
                customer.car.fuel_consumption / 100

            product_cost = calculate_product_cost(
                customer.product_cart,
                shop.products
            )

            fuel_cost_to_home = fuel_cost_to_shop

            total_cost = round(
                fuel_cost_to_shop
                + product_cost
                + fuel_cost_to_home,
                2
            )
            trip_costs[shop.name] = total_cost
            print(f"{customer.name}'s trip"
                  f" to the {shop.name} costs {total_cost}")

        cheapest_shop_name = min(trip_costs, key=trip_costs.get)
        cheapest_shop = None
        for shop in shops:
            if shop.name == cheapest_shop_name:
                cheapest_shop = shop

        if customer.money >= trip_costs[cheapest_shop_name]:
            print(f"{customer.name} rides to {cheapest_shop_name}")

            purchase_and_print_receipt(customer, cheapest_shop)
            print(f"\n{customer.name} rides home")

            remaining_money = customer.money - trip_costs[cheapest_shop_name]
            print(f"{customer.name} now has {remaining_money} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop")
