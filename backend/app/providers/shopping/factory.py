import os

from app.providers.shopping.mock_provider import MockShoppingProvider


class ProviderFactory:

    @staticmethod
    def create():
        provider = os.getenv("SHOPPING_PROVIDER", "mock").lower()

        if provider == "mock":
            return MockShoppingProvider()

        # Future providers
        # if provider == "serpapi":
        #     return SerpAPIProvider()

        raise ValueError(f"Unknown shopping provider: {provider}")