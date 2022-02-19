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
        