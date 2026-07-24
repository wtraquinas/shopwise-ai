from fastapi import FastAPI

from app.api.categories import router as categories_router

from app.api.products import router as products_router

from app.api import health
from app.api import categories
from app.api import products
from app.api import recommend

app = FastAPI(
    title="ShopWise AI",
    version="0.1.0"
)

app.include_router(health.router)
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(recommend.router)

@app.get("/")
def root():
    return {"message": "Welcome to ShopWise AI"}


@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "version": "0.1.0"
    }