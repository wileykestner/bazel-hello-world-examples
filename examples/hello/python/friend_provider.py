from abc import ABCMeta, abstractmethod
from typing import Sequence

class FriendProvider(metaclass=ABCMeta):

    @abstractmethod
    def get_friends() -> Sequence[str]:
        raise NotImplementedError("Subclasses must implement this method")
