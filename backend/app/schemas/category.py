from pydantic import BaseModel

class Category(BaseModel):
    id: str
    title: str
    description: str
    icon: str
    search: str