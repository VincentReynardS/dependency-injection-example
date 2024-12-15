from typing import List, Protocol

from vrs_common.results import ProviderResult

from ..service.model.movie import Movie


class MovieProvider(Protocol):
    def get_movies_by_director(self, director: str) -> ProviderResult[List[Movie]]:
        """
        Gets a list of movies directed by the given director.

        Args:
            director (str): The name of the director of the movies.
        Returns:
            List[Movie]: A list of movies directed by the given director.
        """
        ...
