from fastapi import APIRouter, HTTPException

from app.services.product_service import ProductService

router = APIRouter(
    prefix="/api/products",
    tags=["Products"]
)

service = ProductService()


@router.get("")
def get_products(category: str | None = None):
    """
    Get all products or filter by category.
    Example:
        GET /api/products
        GET /api/products?category=tablets
    """

    products = service.get_products(category)

    return {
        "success": True,
        "data": products
    }


@router.get("/{product_id}")
def get_product(product_id: str):
    """
    Get a single product by ID.
    Example:
        GET /api/products/tablet-001
    """

    product = service.get_product(product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "success": True,
        "data": product
    }