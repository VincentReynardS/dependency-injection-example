from typing import List, Protocol

from .model.movie import Movie


class MovieService(Protocol):
    def get_movies_by_director(director: str) -> List[Movie]:
        pass
