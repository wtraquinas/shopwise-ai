from abc import ABC, abstractmethod

from app.schemas.product import Product


class ShoppingProvider(ABC):

    @abstractmethod
    def search_products(self, category: str) -> list[Product]:
        pass