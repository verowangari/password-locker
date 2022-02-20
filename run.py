from numbers import Number
import string
from random import *

from click import option
from user import User
# from user import Credentials
def create_user(firstname,lastname,username,userpassword):
    newuser= User(firstname,lastname,username,userpassword)
    return newuser
def save_user(user):
    user.save_user()
def delete_user(user):
    user.delete_user()
def find_user(number):
    return User.find_by_number(number)
def display_users():
    return User.display_users
def create_account(accountusername,accountname,accountpassword):
    newaccount=Credentials(accountusername,accountname,accountpassword)
    return newaccount
def save_account(user):
    user.save_account()
def delete_account(user):
    user.delete_account()
def find_account(number):
    return Credentials.find_by_number(number)
def display_accounts():
    return Credentials.display_accounts()
def main():
    while True:
        print("Welcome to Password Locker")
        print("SU -or- LG ")
        option=input()
        if option == "SU":
            print("Create Account")
            print ("_"*10)
            print ("Enter your first name...")
            firstname=input()
            print("Enter your last name")
            lastname=input()
            print("set your username")
            username=input()
            print("Set your password")
            userpassword=input()
            save_user(create_user(firstname,lastname,username,userpassword))
            print("account created successfully. These are the details")
            print ("_"*10)
            print(f"Name:{firstname} {lastname} \nUsername:{username} \nPassword:{userpassword}")
            print("\n \n")
            
    






if __name__ == '__main__':

    main()