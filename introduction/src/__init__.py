from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Container, Singleton

from .service import ServiceContainer
from .simple_application import SimpleApplication


class ApplicationContainer(DeclarativeContainer):
    service_container = Container(ServiceContainer)

    application = Singleton(
        SimpleApplication, user_service=service_container.user_service
    )
