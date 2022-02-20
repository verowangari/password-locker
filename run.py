from numbers import Number
import string
from random import *
from user import Credentials
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
            print("\n Login in to your account")
            print("\n \n")
        elif option =="LG":
            print("your Username..")
            loginUsername=input()
            print("Your password")
            loginPassword=input()
            if find_user(loginPassword):
                print("\n")
                print(" You can create multiple Accounts (AC) and also view Accounts (VC) ")
                print("_"*60)
                print("AC -or- VC")
                choose=input()
                print("\n")
                if choose == "AC":
                    print("Add your Cred Account")
                    print("_"*25)
                    accountusername=loginUsername
                    print("Account Name")
                    accountname=input()
                    print("Generate automatic password (G) or create new password")
                    decision=input()
                    if decision=="G":
                        characters=string.ascii_letters + string.digits
                        accountpassword="".join(choice(characters)for x in range(randint(6,16)))
                        print(f"Password: {accountpassword}")
                    elif decision=="C":
                        print("Enter your password")
                        accountpassword=input()
                    else:
                        print("please put in a valid choice")
                    save_account(create_account)(accountusername,accountname,accountpassword)
                    print("\n")
                    print(f"Username:{accountusername}\nAccount Name:{accountname}\nPassword:{accountpassword}")
                elif choose=="VC":
                    if find_account(accountusername):
                        print("This is the list of your created accounts:")
                        print("_"*25)
                        for user in display_accounts():
                            print(f"Account:{user.accountname}\nPassword:{user.accountpassword}")
                    else:
                        print("Invalid Credentials")
                else:
                    print("please try again!")
                    print("\n")
            else:
                print("Incorrect information,please try again!")
                print("\n")
        else: print("Kindly choose a valid option")
        print("\n")
if __name__ == '__main__':

    main()