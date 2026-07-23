from pydantic import BaseModel

class Product(BaseModel):
    id: str
    title: str
    brand: str
    category: str
    price: float
    currency: str
    rating: float
    review_count: int
    image: str
    store: str
    url: str