import json

from dependency_injector.wiring import Provide, inject

from .service import ServiceContainer, UserService


class SimpleApplication:
    @inject
    def __init__(
        self, user_service: UserService = Provide[ServiceContainer.user_service]
    ) -> None:
        self.user_service = user_service

    def run(self) -> None:
        while True:
            user_id = int(input('Enter a user ID: '))
            user = self.user_service.get_user_by_id(id=user_id)

            print(json.dumps(user))
