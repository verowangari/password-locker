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