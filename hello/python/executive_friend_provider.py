from typing import Sequence
from hello.python.friend_provider import FriendProvider

class ExecutiveFriendProvider(FriendProvider):

    def get_friends(self) -> Sequence[str]:
        return [
            "Aly",
            "Cal",
            "Lidiane",
        ]
