from fastapi import FastAPI
from app.routers import search

app = FastAPI(title="Movie Search Chat (RAG)")

app.include_router(search.router)

@app.get("/")
def home():
    return {"message": "Welcome to the Movie Search API"}