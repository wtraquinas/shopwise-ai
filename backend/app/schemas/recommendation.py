from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    product_id: str