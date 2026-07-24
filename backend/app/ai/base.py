from abc import ABC, abstractmethod

from app.schemas.product import Product


class AIProvider(ABC):

    @abstractmethod
    def generate_recommendation(
        self,
        product: Product
    ) -> dict:
        pass