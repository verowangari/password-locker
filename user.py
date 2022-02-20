import random
import string

class User:
    '''
    Class that generates a new instance of users
    '''
    userslist=[]
    def __init__(self,firstname,lastname,username,password):
        '''
        _init_ :method that helps us define properties for our objectself
        '''
        self.firstname=firstname
        self.lastname=lastname
        self.username=username
        self.password=password
    def save_user(self):
        '''
        save_user:method that saves user info into the userslist
        '''
        User.userlist.append(self)
    def delete_user(self):
        '''
        delete_user: method that deletes a saved user from the userslist
        '''
        User.userslist.remove(self)
        
    @classmethod
    def display_users(cls):
        '''
        return information from the userslist
        '''
        return cls.userslist
    @classmethod
    def find_by_number(cls,number):
        '''
        method that takes in a username and returns a user that matches that number
        '''
        for user in cls.userslist:
            if user.password==number:
                return user
    @classmethod
    def user_exist(cls,number):
        for user in cls.userslist:
            if user.username==number:
                return True
            # return False
    class Credentials:
        '''
        class that generate new instances of Credentials
        '''
        accounts=[]
        def _init_(self,accountusername,accountname,accountpassword):
            '''
            _init_method helps us define properties for our object self
            '''
            self.accountusername=accountusername
            self.accountname=accountname
            self.accountpassword=accountpassword
            def save_account(self):
                '''
                save_account:method that saves users info into accounts
                '''
                Credentials.accounts.append(self)
            def delete_account(self):
                '''
                delete_account: method that deletes a saved credential from accounts
                '''
    @classmethod
    def display_accounts(cls):
        '''
        method to return a list of accounts
        '''
        for account in cls.accounts:
            return cls.display_accounts
    @classmethod
    def find_by_number(cls,number):
            '''
            method that takes in a number and returns a contact that matches that number
            '''
            for account in cls.accounts:
                if account.accountusername==number:
                    return account