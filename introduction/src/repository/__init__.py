from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton

from .user_repository import UserRepository


class RepositoryContainer(DeclarativeContainer):
    user_repository = Singleton(UserRepository)
