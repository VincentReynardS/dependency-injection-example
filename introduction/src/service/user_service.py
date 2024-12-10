from typing import Dict

from dependency_injector.wiring import Provide, inject

from ..provider import ProviderContainer, UserProvider


class UserService:
    @inject
    def __init__(
        self, user_provider: UserProvider = Provide[ProviderContainer.user_provider]
    ):
        self.user_provider = user_provider

    def get_user_by_id(self, id: int) -> Dict[str, str]:
        return self.user_provider.get_user_by_id(id=id)
