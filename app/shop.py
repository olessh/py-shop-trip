from __future__ import annotations
from app.additional_functions import calculate_product_cost


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    @classmethod
    def from_config(cls, config_data: dict) -> Shop:
        return cls(
            config_data["name"],
            config_data["location"],
            config_data["products"]
        )

    def calculate_product_cost(self, product_cart: dict) -> float:
        return calculate_product_cost(product_cart, self.products)
