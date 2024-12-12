from typing import List, Protocol

from .model.movie import Movie


class MovieService(Protocol):
    def get_movies_by_director(self, director: str) -> List[Movie]:
        """
        Gets a list of movies directed by the given director.

        Args:
            director (str): The name of the director of the movies.
        Returns:
            List[Movie]: A list of movies directed by the given director.
        """
        ...
