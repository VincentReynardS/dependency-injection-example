from typing import Dict


class UserRepository:
    def __init__(self) -> None:
        pass

    def get_user_by_id(self, id: int) -> Dict[str, str]:
        return {'id': id, 'name': 'Vincent'}
