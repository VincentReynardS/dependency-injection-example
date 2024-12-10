from dependency_injector.wiring import Provide, inject

from . import ApplicationContainer


@inject
def main(application=Provide[ApplicationContainer.application]) -> None:
    application.run()


if __name__ == '__main__':
    application_container = ApplicationContainer()
    application_container.init_resources()
    application_container.wire(modules=[__name__])

    main()
