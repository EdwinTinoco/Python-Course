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
        *** VIRTUAL WALLET ***
               LOGIN
    """)
    user_name = (input("Username:  ")).upper()
    user_login.append(user_name)
    user_pin = getpass.getpass("\nPIN:    ")
    user_login.append(user_pin)
    return user_login
    

def show_main_menu(main_menu_list, user_login, locked_main_menu = False):
    user_login_op_sel = []
    if len(user_login) <= 2:
        user_login_op_sel = user_login
    else:
        user_login.pop()
        user_login_op_sel = user_login
    option_selected = ""

    if locked_main_menu == False:
        os.system("cls")
        print(f"""
            *** VIRTUAL WALLET ***
                  MAIN MENU


            User: {user_login[0]}


              {main_menu[0]}

              {main_menu[1]}

              {main_menu[2]}

              {main_menu[3]}
            """)
        option_selected = input("\n\nWhat option do you want to select?: ")
        if option_selected == "corona":
            return show_main_menu(main_menu_list, user_login, locked_main_menu = True)

        elif option_selected == "anticorona":        
            return show_main_menu(main_menu_list, user_login)
        else:
            user_login_op_sel.append(option_selected)                
            return user_login_op_sel
    else:
        os.system("cls")
        print(f"""
            *** VIRTUAL WALLET ***
                  MAIN MENU


            User: {user_login[0]}


            Your account was FREEZING!!!...
            you cannot do any transaction!
            """)
        while option_selected != "anticorona":
            option_selected = input("\n\nWhat is the magic word to UNFREEZE your account???: ")            
        else:
            return show_main_menu(main_menu_list, user_login)


def show_sub_menu(sub_menu_list):
    sub_menu_op_sel = 0

    print(f"""
        {sub_menu[0]}

        {sub_menu[1]}
    """)

    while (sub_menu_op_sel != 1) and (sub_menu_op_sel != 2):
        sub_menu_op_sel = int(input("\n\nWhat option do you want to select?: "))
    else:
        return sub_menu_op_sel


# Classes Section
class UserOptionSelected:     
    def __init__(self, user_info, balance):
        self.user_login = user_info[0:2]        
        self.option_selected = user_info[2]
        self.balance = balance

    def check_balance(self):
        os.system("cls")
        print(f"""
            *** VIRTUAL WALLET ***
            User: {self.user_login[0]}



            Option selected 
            {main_menu[int(self.option_selected) - 1]}


            Your balance is: ${self.balance}
        """)
        op_sel_sub_menu = show_sub_menu(sub_menu)
        if op_sel_sub_menu == 1:
            self.option_selected = (show_main_menu(main_menu, self.user_login))[2] 
        elif op_sel_sub_menu == 2:
            sys.exit()

    def withdrawal(self):
        os.system("cls")
        print(f"""
            *** VIRTUAL WALLET ***
            User: {self.user_login[0]}



            Option selected
            {main_menu[int(self.option_selected) - 1]}              
        """)                
        self.balance -= float( input("\nWithdrawal amount: $"))
        print("\n\n")
        op_sel_sub_menu = show_sub_menu(sub_menu)
        if op_sel_sub_menu == 1:
            self.option_selected = (show_main_menu(main_menu, self.user_login))[2]
        elif op_sel_sub_menu == 2:
            sys.exit()

    def deposit(self):
        os.system("cls")
        print(f"""
             *** VIRTUAL WALLET ***
             User: {self.user_login[0]}



            Option selected
            {main_menu[int(self.option_selected) - 1]}                
        """)                
        self.balance += float(input("\nDeposit amount: $"))  
        print("\n\n")              
        op_sel_sub_menu = show_sub_menu(sub_menu)
        if op_sel_sub_menu == 1:
            self.option_selected = (show_main_menu(main_menu, self.user_login))[2]
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


user_one = WalletTransaction(show_main_menu(main_menu, show_login()), 10000)
user_one.transaction()

user_two = WalletTransaction(show_main_menu(main_menu, show_login()), 5000)
user_two.transaction()

print(f"""

    User one: {user_one.user_login[0]} 
    Balance:  ${user_one.balance}


    User two: {user_two.user_login[0]}
    Balance:  ${user_two.balance}
    """)
