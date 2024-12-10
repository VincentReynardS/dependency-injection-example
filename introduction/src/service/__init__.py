from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Container, Singleton

from ..provider import ProviderContainer
from .user_service import UserService


class ServiceContainer(DeclarativeContainer):
    provider_container = Container(ProviderContainer)

    user_service = Singleton(
        UserService, user_provider=provider_container.user_provider
    )
