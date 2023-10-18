from typing import Sequence
from hello.python.friend_provider import FriendProvider
from hello.python.mobile_friend_provider import MobileFriendProvider
from hello.python.executive_friend_provider import ExecutiveFriendProvider

class Hello(object):
    def __init__(self, friend_providers: Sequence[FriendProvider]) -> None:
        super().__init__()
        self._friend_providers = friend_providers
    
    def main(self):
       friends = [friend for fp in self._friend_providers for friend in fp.get_friends()]
       sorted_friends = sorted(friends)
       for friend in sorted_friends:
           print(f"hello {friend}")


if __name__ == "__main__":
    all_friend_providers = [
        MobileFriendProvider(),
        ExecutiveFriendProvider(),
    ]
    
    hello = Hello(friend_providers=all_friend_providers)
    hello.main()
