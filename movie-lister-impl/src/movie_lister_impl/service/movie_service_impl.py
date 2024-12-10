from dependency_injector.wiring import Provide, inject
from movie_lister_api.provider.movie_provider import MovieProvider
from movie_lister_api.service.model.movie import Movie
from movie_lister_api.service.movie_service import MovieService

from ..provider import ProviderContainer


class MovieServiceImpl(MovieService):
    @inject
    def __init__(
        self, movie_provider: MovieProvider = Provide[ProviderContainer.movie_provider]
    ):
        self.movie_provider = movie_provider

    def get_movies_by_director(self, director: str) -> Movie:
        return self.movie_provider.get_movies_by_director(director=director)
