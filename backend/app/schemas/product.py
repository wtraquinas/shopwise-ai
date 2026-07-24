from pydantic import BaseModel


class Product(BaseModel):
    id: str
    category: str

    brand: str
    title: str

    price: float
    currency: str

    rating: float
    review_count: int

    image: str
    store: str
    url: str

    description: str

    # Future AI fields
    summary: str | None = None
    pros: list[str] = []
    cons: list[str] = []