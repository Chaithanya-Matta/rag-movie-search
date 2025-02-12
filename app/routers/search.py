from fastapi import APIRouter, Depends
# from app.services.openai_api import generate_rag_response
# from app.services.vector_db import search_movies

router = APIRouter()

@router.get("/search")
def search_movie(query: str):
    # similar_movies = search_movies(query)
    # response = generate_rag_response(query, similar_movies)
    # return {"movies": similar_movies, "response": response}
    return "test"
