from typing import Protocol

from ..service.model.movie import Movie


class MovieProvider(Protocol):
    def get_movie_by_director(director: str) -> Movie:
        pass
