from pydantic import BaseModel

class Movie(BaseModel):
    id: int
    title: str
    overview: str
    genres: list[str]