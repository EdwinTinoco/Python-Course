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
import os
#import sys

#Global variables
main_menu = [
            "1. Check Balance",
            "2. Withdrawal Cash",
            "3. Deposit Cash",
            "4. Exit"
            ]


# Classes Section
class UserOptionSelected: 
    # Global variable inside the main class
    balance = 5000   

    def __init__(self, option_selected):
        self.option_selected = option_selected

    def transaction(self):
        pass

class WalletTransaction(UserOptionSelected):
    def transaction(self):
        #if self.option_selected < 4:
            while self.option_selected < 4:
                if self.option_selected == 1:
                    os.system("cls")
                    print(f"""
                        Option selected 
                        {main_menu[self.option_selected - 1]}

                        Your balance is: ${self.balance}
                    """)
                    return_main_menu = input("Return main menu y/n: ")
                    if return_main_menu.lower() == 'y':
                        self.option_selected = show_main_menu(main_menu) 

                elif self.option_selected == 2:
                    os.system("cls")
                    print(f"""
                        Option selected
                        {main_menu[self.option_selected - 1]}              
                    """)
                    withdrawal_amount = input("Withdrawal amount: $")
                    self.balance -= int(withdrawal_amount)
                    return_main_menu = input("Return main menu y/n: ")
                    if return_main_menu.lower() == 'y':
                        self.option_selected = show_main_menu(main_menu) 

                elif self.option_selected == 3:
                    os.system("cls")
                    print(f"""
                        Option selected
                        {main_menu[self.option_selected - 1]}                
                    """)
                    deposit_amount = input("Deposit amount: $")
                    self.balance += int(deposit_amount)
                    return_main_menu = input("Return main menu y/n: ")
                    if return_main_menu.lower() == 'y':
                        self.option_selected = show_main_menu(main_menu)
        # elif self.option_selected > 4:
        #     print("That option doesn't exist!")            
        # else:
        #     sys.exit()                

# Functions Section
def show_main_menu(main_menu_list):
    os.system("cls")
    print(f"""
        *** Virtual Wallet ***
              Main Menu

        {main_menu[0]}
        {main_menu[1]}
        {main_menu[2]}
        {main_menu[3]}
        """)

    option_selected = int(input("What option do you want to select?: "))
    return option_selected

user_op_sel = WalletTransaction(show_main_menu(main_menu))
user_op_sel.transaction()
