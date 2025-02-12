import openai
import weaviate
from app.core.config import settings

client = weaviate.Client(settings.VECTOR_DB_URL)

def embed_movie_description(description: str):
    response = openai.embeddings.create(
        model="text-embedding-3-small",
        input=description
    )
    return response["data"][0]["embedding"]

def store_movie_in_vector_db(movie):
    embedding = embed_movie_description(movie.overview)
    client.data_object.create(
        data_object={"title": movie.title, "overview": movie.overview, "genres": movie.genres},
        class_name="Movie",
        vector=embedding
    )
