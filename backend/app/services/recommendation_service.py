import json

from openai import OpenAI

from app.config import settings
from app.prompts import RECOMMENDATION_PROMPT
from app.services.product_service import ProductService


class RecommendationService:

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

        self.products = ProductService()

    def recommend(self, product_id):

        product = self.products.get_product(product_id)

        if product is None:
            raise ValueError("Product not found")

        response = self.client.responses.create(
            model=settings.OPENAI_MODEL,
            input=[
                {
                    "role": "system",
                    "content": RECOMMENDATION_PROMPT,
                },
                {
                    "role": "user",
                    "content": product.model_dump_json(indent=2),
                },
            ],
        )

        return json.loads(response.output_text)