import openai
from ..core.config import settings

def generate_rag_response(query: str, similar_movies: list):
    movie_context = "\n".join([f"{m['title']}: {m['overview']}" for m in similar_movies])

    prompt = f"""
    You are a movie assistant. A user asked: "{query}".
    Based on the following movies:
    {movie_context}

    Provide a helpful response with recommendations.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]
