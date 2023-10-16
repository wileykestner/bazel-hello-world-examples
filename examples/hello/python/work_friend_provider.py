from typing import Sequence
from examples.hello.python.friend_provider import FriendProvider

class WorkFriendProvider(FriendProvider):

    def get_friends(self) -> Sequence[str]:
        return [
            "Aly",
            "Cal",
            "Lidiane",
        ]
