from typing import Dict

from dependency_injector.wiring import Provide, inject

from ..repository import RepositoryContainer, UserRepository


class UserProvider:
    @inject
    def __init__(
        self,
        user_repository: UserRepository = Provide[RepositoryContainer.user_repository],
    ) -> None:
        self.user_repository = user_repository

    def get_user_by_id(self, id: int) -> Dict[str, str]:
        """
        Args:
            id (int): the id of the user
        Return:
            (Dict)
        """
        return self.user_repository.get_user_by_id(id=id)
