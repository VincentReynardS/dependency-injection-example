from pydantic import BaseModel


class Movie(BaseModel):
    """
    A data class containing details of a movie.
    """

    title: str
    year: int
    director: str
