import json
from pathlib import Path

from app.schemas.product import Product

class ProductService:

    def __init__(self):
        self.file_path = (
            Path(__file__).resolve().parent.parent
            / "data"
            / "products.json"
        )

    def _load_products(self) -> list[Product]:
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return [Product(**item) for item in data]

    def get_products(
        self,
        category: str | None = None
    ) -> list[Product]:

        products = self._load_products()

        if category is None:
            return products

        return [
            product
            for product in products
            if product.category == category
        ]

    def get_product(
        self,
        product_id: str
    ) -> Product | None:

        products = self._load_products()

        for product in products:
            if product.id == product_id:
                return product

        return None