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
def test_init(self):
        '''
        test_init: test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"Veronica")
        self.asserEqual(self.new_user.password,"2022")
def test_save_user(self):
    '''
    test_save_user: test case to test if the user object is saved into the user list
    '''
    self.new_user.save_user()#save new contact
    self.asserEqual(len(User.user_list),1)
    