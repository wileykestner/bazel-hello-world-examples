import unittest
from hello.python.executive_friend_provider import ExecutiveFriendProvider


class TestExecutiveFriendProvider(unittest.TestCase):
    def setUp(self) -> None:
        self._subject = ExecutiveFriendProvider()
        return super().setUp()

    def test_denise_is_executive_friend(self):
        excutive_friends = self._subject.get_friends()
        self.assertTrue("Denise" in excutive_friends)

    def test_noah_is_executive_friend(self): 
        excutive_friends = self._subject.get_friends()
        self.assertTrue("Noah" in excutive_friends)
    
    def test_patrick_is_executive_friend(self): 
        excutive_friends = self._subject.get_friends()
        self.assertTrue("Parker" in excutive_friends)
    
if __name__ == "__main__":
    unittest.main()
