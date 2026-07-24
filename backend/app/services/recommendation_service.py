import json

from openai import OpenAI

from app.config import settings
from app.services.product_service import ProductService


class RecommendationService:

    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.products = ProductService()

    def recommend(self, product_id: str):

        product = self.products.get_product(product_id)

        if product is None:
            raise ValueError("Product not found")

        prompt = f"""
You are an expert consumer electronics reviewer.

Return ONLY valid JSON.

Schema:

{{
    "score": 0-10,
    "summary": "...",
    "pros": [],
    "cons": [],
    "best_for": []
}}

Product:

{product.model_dump_json(indent=2)}
"""

        response = self.client.responses.create(
            model="gpt-5.5",
            input=prompt,
        )

        return json.loads(response.output_text)