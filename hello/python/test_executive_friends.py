import unittest
from hello.python.executive_friend_provider import ExecutiveFriendProvider


class TestExecutiveFriendProvider(unittest.TestCase):
    def setUp(self) -> None:
        self._subject = ExecutiveFriendProvider()
        return super().setUp()

    def test_stewart_is_executive_friend(self):
        excutive_friends = self._subject.get_friends()
        self.assertTrue("Stewart" in excutive_friends)

    def test_aly_is_executive_friend(self): 
        excutive_friends = self._subject.get_friends()
        self.assertTrue("Aly" in excutive_friends)
    
    def test_cal_is_executive_friend(self): 
        excutive_friends = self._subject.get_friends()
        self.assertTrue("Cal" in excutive_friends)
    
    def test_lidiane_is_executive_friend(self): 
        excutive_friends = self._subject.get_friends()
        self.assertTrue("Lidiane" in excutive_friends)

if __name__ == "__main__":
    unittest.main()