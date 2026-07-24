from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.categories import router as categories_router
from app.api.products import router as products_router
from app.api.recommend import router as recommend_router

app = FastAPI(
    title="ShopWise AI",
    version="0.1.0"
)

app.include_router(health_router)
app.include_router(categories_router)
app.include_router(products_router)
app.include_router(recommend_router)


@app.get("/")
def root():
    return {"message": "Welcome to ShopWise AI"}