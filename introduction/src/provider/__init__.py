from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Container, Singleton

from ..repository import RepositoryContainer
from .user_provider import UserProvider


class ProviderContainer(DeclarativeContainer):
    repository_container = Container(RepositoryContainer)

    user_provider = Singleton(
        UserProvider, user_repository=repository_container.user_repository
    )
