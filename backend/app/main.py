from fastapi import FastAPI

app = FastAPI(
    title="ShopWise AI",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to ShopWise AI"}

@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "version": "0.1.0"
    }