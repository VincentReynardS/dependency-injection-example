from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Container, Singleton

from ..provider import ProviderContainer
from .movie_service_impl import MovieServiceImpl


class ServiceContainer(DeclarativeContainer):
    provider_container = Container(ProviderContainer)

    movie_service = Singleton(
        MovieServiceImpl, movie_provider=provider_container.movie_provider
    )
