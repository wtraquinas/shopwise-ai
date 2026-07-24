from fastapi import APIRouter, HTTPException

from app.schemas.category import Category
from app.services.category_service import CategoryService

router = APIRouter(
    prefix="/api/categories",
    tags=["Categories"]
)

service = CategoryService()


@router.get("")
def get_categories():
    return {
        "success": True,
        "data": service.get_categories()
    }


@router.get("/{category_id}")
def get_category(category_id: str):

    category = service.get_category(category_id)

    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return {
        "success": True,
        "data": category
    }