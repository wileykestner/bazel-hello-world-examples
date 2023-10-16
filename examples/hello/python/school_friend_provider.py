from typing import Sequence
from examples.hello.python.friend_provider import FriendProvider


class SchoolFriendProvider(FriendProvider):

    def get_friends(self) -> Sequence[str]:
        return [
            "Alice",
            "Bob",
            "Chester",
        ]
