from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    product_id: str


class RecommendationResponse(BaseModel):
    score: float
    summary: str
    pros: list[str]
    cons: list[str]
    best_for: list[str]