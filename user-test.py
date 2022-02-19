import unittest
from user import User 

class Testuser(unittest.TestCase):
    '''
    Test class that defines test cases for user class behaviors.
    unittest.TestCase: Testcase class that helps in creating test cases
    '''
def setUp(self):
    '''
    setUp: method that runs before each testcases.
    '''
    self.new_user=User("Veronica","Rodriguez","2022")
    