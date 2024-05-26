################References###############
#https://realpython.com/python3-object-oriented-programming/
#https://www.w3schools.com/python/
#https://youtu.be/xTh-ln2XhgU(YOUTUBE video of 23min, 23sec)
######################################

import random # Because later i want to import account no. and password randomly

class Account: # Initialize account attributes
    def __init__(self, account_number, account_password, account_type): #initializing the account with various parameters
        self.account_number = account_number
        self.password = account_password 
        self.account_type = account_type
        self.balance = 0 # we will assume our current balance as 0

    def deposit_amount(self, balance):
        if balance > 0:
            self.balance += balance # Deposit money into the account
            print(f"Deposited Nu.{balance:.2f}. New balance: Nu.{self.balance:.2f}") # shows the deposited amount and current balance.
        else:
            print("Invalid deposit amount.") 

    def withdraw_money(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount #  Withdraw money from the account
            print(f"Withdrew Nu.{amount:.2f}. Your new balance is : Nu.{self.balance:.2f}")
        else:
            print("Insufficient balance!")

    def transfer_money(self, amount, another_account):  # Transfer money to another account
        if 0 < amount <= self.balance:
            self.balance -= amount # the transfer_amount is deducted from the current_amount 
            another_account.balance += amount # Adds the transfer_amount to the target_amount 
            print(f"Transferred Nu.{amount:.2f} to account {another_account.account_number}.")
        else:
            print("Insufficient amount.")

    def check_amount(self):  #Checking the current balance of the account
        print(f"Current balance: Nu.{self.balance:.2f}")

class Bank:
    def __init__(self):
        self.accounts = {} # Dictonary that will store the account information

    def create_account(self, account_type):
        account_number = str(random.randint(100000, 999999))# randomly generates the account number for user in between the given range
        account_password = str(random.randint(1000, 9999))# randomly generates the random password for the user in between the given range
        self.accounts[account_number] = Account(account_number, account_password, account_type) # helps store the information in new account 
        print(f"You have successfully created an Account. Your Account Number: {account_number}, Your account Password: {account_password}. Use this information to later login!!") # users account number and password is displayed

    def account_login(self, account_number, account_password):
        account = self.accounts.get(account_number)
        if account and account.password == account_password:
            print("Login successful!")
            return account
        print("You have entered a wrong account number or incorrect password!")
        return None

def main(): #Main function to run the banking application
    bank = Bank() 

    while True: # The main loop that will keep the program running until the user enter to exit.
        option = input("\n----------WELCOME TO Tandin BANK---------\na. Open Account\nb. Login\nc. Exit\nEnter your choice : ") # where it display 3 option for the user to choose
        if option == "a":
            account_type = input("Enter the account type you want (P for Personal/ B for Business): ").lower()
            if account_type in ["p", "b"]:
                bank.create_account(account_type)
            else:
                print("No such account exist!")
        elif option == "b":
            account_number = input("Enter your account number: ")
            account_password = input("Enter your password: ")
            account = bank.account_login(account_number, account_password)
            if account:
                while True: 
                    user_choice = input("\n01. Check Balance\n02. Deposit\n03. Withdraw\n04. Transfer\n05. Logout\nEnter your choice: ")
                    if user_choice == "01":
                        account.check_balance()
                    elif user_choice == "02":
                        account.deposit(float(input("Enter amount to deposit: ")))
                    elif user_choice == "03":
                        account.withdraw(float(input("Enter amount to withdraw: ")))
                    elif user_choice == "04":
                        another_account_number = input("Enter account number that you want to transfer: ")
                        holder_account = bank.accounts.get(another_account_number)
                        if holder_account:
                            account.transfer(float(input("Enter amount to transfer: ")), holder_account)
                        else:
                            print("These account does not exist.")
                    elif user_choice == "05":
                        print("You have logged out successfully. Thank you!")
                        break # break out of the loop 
                    else:
                        print("Invalid choice! Please select a valid option.")

        elif option == "c":
            print("Exiting the application. Thank you!")
            break # exiting the application
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main() # The main function which executes the code.
