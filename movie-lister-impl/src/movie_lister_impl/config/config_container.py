from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton

from .csv_movie_config import CSVMovieConfig


class ConfigContainer(DeclarativeContainer):
    csv_movie_config = Singleton(CSVMovieConfig)
