from abc import ABC, abstractmethod
from typing import Any


class BaseRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> Any | None:
        raise NotImplementedError("This method should be implemented by the class")

    @abstractmethod
    def create(self, data: Any) -> Any:
        raise NotImplementedError("This method should be implemented by the class")
