"""
Create a Virtual Wallet in Python

- A user should be able to interact with your wallet in the following ways:
  - Choices made in a menu screen
  - Check Balance
  - Withdrawal Cash
  - Deposit Cash
  - Go back to the main menu
  - Exit the Program

Try using OOP principles to build this program. I will be looking at how your control structures 
( the flow of your program, function routing, etc ) come together.

- Bonus
  - Attempt to use a Flask API to persist account information.
"""

# With Users version*********************************************************************
import os
import sys
import getpass


#Global variables Section
main_menu = [
            "1. Check Balance",
            "2. Withdrawal Cash",
            "3. Deposit Cash",
            "4. Exit"
            ]

sub_menu = [
            "1. Return main menu",
            "2. Exit"
            ]


# Functions Section
def show_login():
    os.system("cls")
    user_login = []

    print(f"""
        *** Virtual Wallet ***
               Login
    """)
    user_name = input("Username:  ")
    user_login.append(user_name)
    user_pin = getpass.getpass("\nPIN:    ")
    user_login.append(user_pin)
    return user_login
    

def show_main_menu(main_menu_list, user_login, lockedOut = False):
    print(lockedOut)
    os.system("cls")
    print(f"""
        *** Virtual Wallet ***
              Main Menu


        User: {user_login[0]}


        {main_menu[0]}

        {main_menu[1]}

        {main_menu[2]}

        {main_menu[3]}
        """)
    option_selected = input("\n\nWhat option do you want to select?: ")
    if option_selected == "corona":
        print(f"""
            'Your Account was freeze, you can not to do any transaction!'
        """)  
        # option_selected = str(len(main_menu_list))
        show_main_menu(main_menu_list, user_login, lockedOut = True)
    
    return option_selected


def show_sub_menu(sub_menu_list):
    print(f"""
        {sub_menu[0]}

        {sub_menu[1]}
    """)

    option_selected = int(input("\n\nWhat option do you want to select?: "))
    return option_selected


# Classes Section
class UserOptionSelected:     
    def __init__(self, user_login, option_selected, balance):
        self.user_login = user_login        
        self.option_selected = option_selected
        self.balance = balance

    def check_balance(self):
        os.system("cls")
        print(f"""
            *** Virtual Wallet ***
            User: {self.user_login[0]}



            Option selected 
            {main_menu[int(self.option_selected) - 1]}


            Your balance is: ${self.balance}
        """)
        op_sel_sub_menu = show_sub_menu(sub_menu)
        if op_sel_sub_menu == 1:
            self.option_selected = show_main_menu(main_menu, user_login)               
        elif op_sel_sub_menu == 2:
            sys.exit()

    def withdrawal(self):
        os.system("cls")
        print(f"""
            *** Virtual Wallet ***
            User: {self.user_login[0]}



            Option selected
            {main_menu[int(self.option_selected) - 1]}              
        """)                
        self.balance -= float( input("\nWithdrawal amount: $"))
        print("\n\n")
        op_sel_sub_menu = show_sub_menu(sub_menu)
        if op_sel_sub_menu == 1:
            self.option_selected = show_main_menu(main_menu, user_login)
        elif op_sel_sub_menu == 2:
            sys.exit()

    def deposit(self):
        os.system("cls")
        print(f"""
             *** Virtual Wallet ***
             User: {self.user_login[0]}



            Option selected
            {main_menu[int(self.option_selected) - 1]}                
        """)                
        self.balance += float(input("\nDeposit amount: $"))  
        print("\n\n")              
        op_sel_sub_menu = show_sub_menu(sub_menu)
        if op_sel_sub_menu == 1:
            self.option_selected = show_main_menu(main_menu, user_login)
        elif op_sel_sub_menu == 2:
            sys.exit()        
           

class WalletTransaction(UserOptionSelected):
    def transaction(self):   
        while int(self.option_selected) < len(main_menu): 
            if int(self.option_selected) == 1:   
                self.check_balance()

            elif int(self.option_selected) == 2:
                self.withdrawal()                

            elif int(self.option_selected) == 3:
                self.deposit()      


user_login = show_login()
user_one = WalletTransaction(user_login, show_main_menu(main_menu, user_login), 10000)
user_one.transaction()

# user_two = WalletTransaction(show_main_menu(main_menu),5000)
# user_two.transaction()

# print(user_one.balance)
# print(user_two.balance)