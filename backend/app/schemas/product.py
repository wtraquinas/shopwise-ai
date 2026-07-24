from pydantic import BaseModel


class Product(BaseModel):
    id: str
    name: str
    category: str
    description: str
    price: float
    rating: float

    review_count: int | None = None
    store: str | None = None
    url: str | None = None
    image: str | None = None