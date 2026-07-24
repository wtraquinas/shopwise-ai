from fastapi import APIRouter, HTTPException

from app.ai.openai_provider import OpenAIProvider
from app.schemas.recommendation import RecommendationRequest
from app.services.product_service import ProductService

router = APIRouter(
    prefix="/api/recommend",
    tags=["Recommendations"]
)

provider = OpenAIProvider()
products = ProductService()


@router.post("")
def recommend(request: RecommendationRequest):

    product = products.get_product(request.product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    recommendation = provider.generate_recommendation(product)

    return {
        "success": True,
        "data": recommendation
    }