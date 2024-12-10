from pydantic import BaseModel


class MovieEntity(BaseModel):
    title: str
    year: int
    director: str
