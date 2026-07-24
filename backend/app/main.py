from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.categories import router as categories_router
from app.api.products import router as products_router
from app.api.recommend import router as recommend_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="ShopWise AI",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://your-frontend.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(categories_router)
app.include_router(products_router)
app.include_router(recommend_router)


@app.get("/")
def root():
    return {"message": "Welcome to ShopWise AI"}