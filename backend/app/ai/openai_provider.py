import json
import os

from openai import OpenAI

from app.schemas.product import Product
from app.ai.prompts import RECOMMENDATION_PROMPT


class OpenAIProvider:

    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def _product_to_text(self, product: Product) -> str:

        return f"""
Title: {product.title}
Brand: {product.brand}
Category: {product.category}
Price: {product.currency} {product.price}
Rating: {product.rating}/5 ({product.review_count} reviews)

Description:
{product.description}
"""

    def generate_recommendation(
        self,
        product: Product
    ) -> dict:

        prompt = (
            RECOMMENDATION_PROMPT
            + "\n\n"
            + self._product_to_text(product)
        )

        response = self.client.responses.create(
            model="gpt-5.5",
            input=prompt
        )

        text = response.output_text

        return json.loads(text)