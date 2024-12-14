from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Container, Singleton

from ..config import ConfigContainer
from .csv_movie_provider_impl import CSVMovieProviderImpl


class ProviderContainer(DeclarativeContainer):
    config_container = Container(ConfigContainer)

    movie_provider = Singleton(
        CSVMovieProviderImpl, csv_movie_config=config_container.csv_movie_config
    )
