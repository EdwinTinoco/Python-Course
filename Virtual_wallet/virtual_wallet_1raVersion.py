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
import sys


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

    option_selected = int(input("\n\nWhat option do you want to select?: "))
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
    # Global atributte inside the main class
    balance = 5000   

    def __init__(self, option_selected):
        self.option_selected = option_selected 
           

class WalletTransaction(UserOptionSelected):
    def transaction(self):        
        while self.option_selected < len(main_menu):
            if self.option_selected == 1:
                os.system("cls")
                print(f"""
                    *** Virtual Wallet ***

                    Option selected 
                    {main_menu[self.option_selected - 1]}


                    Your balance is: ${self.balance}
                """)
                op_sel_sub_menu = show_sub_menu(sub_menu)
                if op_sel_sub_menu == 1:
                    self.option_selected = show_main_menu(main_menu)
                elif op_sel_sub_menu == 2:
                    sys.exit()
                else:
                    print("That option is wrong!") 

            elif self.option_selected == 2:
                os.system("cls")
                print(f"""
                    *** Virtual Wallet ***

                    Option selected
                    {main_menu[self.option_selected - 1]}              
                """)                
                self.balance -= int( input("\nWithdrawal amount: $"))
                op_sel_sub_menu = show_sub_menu(sub_menu)
                if op_sel_sub_menu == 1:
                    self.option_selected = show_main_menu(main_menu)
                elif op_sel_sub_menu == 2:
                    sys.exit()
                else:
                    print("That option is wrong!") 

            elif self.option_selected == 3:
                os.system("cls")
                print(f"""
                    *** Virtual Wallet ***

                    Option selected
                    {main_menu[self.option_selected - 1]}                
                """)                
                self.balance += int(input("\nDeposit amount: $"))                
                op_sel_sub_menu = show_sub_menu(sub_menu)
                if op_sel_sub_menu == 1:
                    self.option_selected = show_main_menu(main_menu)
                elif op_sel_sub_menu == 2:
                    sys.exit()
                else:
                    print("That option is wrong!")                    


user_op_sel = WalletTransaction(show_main_menu(main_menu))
user_op_sel.transaction()
