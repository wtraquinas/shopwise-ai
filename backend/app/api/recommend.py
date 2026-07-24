from fastapi import APIRouter, HTTPException

from app.schemas.recommendation import (
    RecommendationRequest,
    RecommendationResponse,
)

from app.services.recommendation_service import RecommendationService

router = APIRouter(
    prefix="/api/recommend",
    tags=["AI"],
)

service = RecommendationService()


@router.post("", response_model=RecommendationResponse)
def recommend(request: RecommendationRequest):

    try:
        return service.recommend(request.product_id)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )