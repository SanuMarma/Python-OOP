import random
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, email, address, account_type):
        super().__init__(name, email, address)
        self.account_type = account_type
        self.balance = 0
        self.transaction_history = []
        self.loan = 0
        self.loan_amount = 0
        self.account_number = random.randint(10000000, 99999999)
    
    def createUser(self, userInfo, bank):
        bank.create_user_account(userInfo)
    
    def deposit(self, amount, bank):
            self.balance += amount
            bank.balance += amount
            print(f'Deposit Successfully! New Balance: {self.balance}')
            self.transaction_history.append(f'Deposit Amount: {amount}, Current Balance: {self.balance}')
    
    def withdraw(self, amount, bank):
        if(amount > self.balance):
            print("Withdrawl amount exceeded")
        elif amount > bank.balance:
            print("Sorry, The Bank is bankrupt")
        else:
            self.balance -= amount
            bank.balance -= amount
            print(f'Withdrawl Successfully! New Balance: {self.balance}')
            self.transaction_history.append(f'Withdraw Amount: {amount}, Current Balance: {self.balance}')

    def check_balance(self):
        print(f'Your current balance is {self.balance}')
    
    def check_transaction_history(self):
        print("-----------")

        for history in self.transaction_history:
            print(history)
        
        print("-----------")
    
    
    def take_loan(self, amount, bank):
        if(self.loan < 2):
            bank.receive_loan(amount, self)
        else:
            print("Sorry, loan limit exceeded.")

    def sendMoney(self, reciever_email, amount, bank):
        bank.transfer(self.email, reciever_email, amount)
    
    def receive_loan(self, amount, bank):
        self.balance += amount
        bank.balance += amount
        self.transaction_history.append(f'Received Amount: {amount}, Current Balance: {self.balance}')
        return f'Transfer Received Successfully! New Balance: {self.balance}.'
       

class Admin(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)

    def createAdmin(self, adminInfo, bank):
        bank.create_admin_account(adminInfo)

    def remove_user(self, email, bank):
        bank.delete_user_account(email)
    
    def view_users(self, bank):
        bank.view_all_users()
        
    def check_total_balance(self, bank):
        print("Total balance of the bank:", bank.balance)
    
    def check_total_loan(self, bank):
        print("Total Loan Amount of the bank:", bank.loan_amount)
    
    def loan_feature(self, decision, bank):
        bank.loan = decision


class Bank:
    def __init__(self, name, bank_amount):
        self.name = name
        self.balance = bank_amount
        self.loan = True
        self.loan_amount = 0
        self.users = []
        self.admins = []
        

    def create_user_account(self, user):
        self.users.append(user)
        print("Account created successfully!")

    def create_admin_account(self, admin):
        self.admins.append(admin)
        print("Account created successfully!")

    def find_user(self, email):
        for userAcc in self.users:
            if email == userAcc.email:
                return userAcc
        return None

    def find_admin(self, email):
        for adminAcc in self.admins:
            if email == adminAcc.email:
                return True
        return False
    
    def transfer(self, sender_email, reciever_email, amount):
        sender = self.find_user(sender_email)
        reciever = self.find_user(reciever_email)

        if sender is not None and reciever is not None:
            if sender.balance > amount:
                reciever.balance += amount
                sender.balance -= amount
                print(
                    f"From {sender_email}\nTo {reciever_email}\n{amount} Tk Transfer Succesfully!"
                )
            else:
                print("Not Enough Balance")
        else:
            print("Account Not Found")
    
    def receive_loan(self, amount, user):
        if(self.loan == True):
            if amount > self.balance:
                print("Sorry, Loan amount exceeded")
            else:
                user.loan += 1
                user.loan_amount += amount
                user.balance += amount
                self.balance -= amount
                self.loan_amount += amount
                print(f"Successfully Loan Recieved. New Balance: {user.balance}")
                user.transaction_history.append(f'Loan Amount: {amount} Current Balance: {user.balance}')
        else:
            print("Sorry cannot give Loan")
    
    def view_all_users(self):
        print('==================')
        
        for user in bank.users:
            print(f"""
                    Account No: {user.account_number}
                    Name: {user.name} 
                    Email: {user.email} 
                    Balance: {user.balance} 
                    Loan Amount: {user.loan_amount}
                """)
        
        print('==================')

    def delete_user_account(self, email):
        for userAcc in self.users:
            if email == userAcc.email:
                self.users.remove(userAcc)
                print("Account deleted successfully!")
            else:
                print(f"User not Found")

            

bank = Bank('Phitron Bank', 100000000)

def customerMenu(customer):
  
    while True:
        
        print(f'\n-----Welcome {customer.name} as a Customer-----\n')
        print("1. Deposit Amount")
        print("2. Withdraw Amount")
        print("3. Check Balance")
        print("4. Check Transaction History")
        print("5. Take Loan")
        print("6. Transfer Amount")
        print("7. Exit")

        choice = int(input("Enter an option: "))
        
        if choice == 1:
            deposit = int(input("Enter deposit amount: "))
            customer.deposit(deposit, bank)
        elif choice == 2:
            withdraw = int(input("Enter withdraw amount: "))
            customer.withdraw(withdraw, bank)
        elif choice == 3:
            customer.check_balance()
        elif choice == 4:
            customer.check_transaction_history()
        elif choice == 5:
            amount = int(input("Enter loan amount: "))
            customer.take_loan(amount, bank)

        elif choice == 6:
            reciever_email = input("Reciever email : ")
            amount = int(input("Amount : "))
            customer.sendMoney(reciever_email, amount, bank)

        elif choice == 7:
            print("Exit")
            break
        
        else:
            print("Invalid Input")



def customerLogin():
    while True:
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit")

        choice = int(input("Enter an option : "))
        if choice == 1:
            email = input("Please Enter Your Email : ")
            if bank.find_user(email) is not None:
                customerMenu(bank.find_user(email))
            else:
                print("Email Not Exist")

        elif choice == 2:
            name = input('Enter your Name : ')
            email = input('Enter your Email : ')
            address = input('Enter your Address : ')
            print("Account Type : 'Savings ? Current'")
            account_type = input('Enter your Account Type : ')

            if bank.find_user(email) is not None:
                print(f"Sorry {email} Already Exist")
            else:
                customer = Customer(name=name, email=email, address=address, account_type=account_type)

                customer.createUser(customer, bank)
                customerMenu(customer)

        elif choice == 3:
            break

        else:
            print("Invalid Input")
        
# ------Admin-----------------------

def adminMenu():
    name = input('Enter Your Name : ')
    email = input('Enter your Email : ')
    address = input('Enter your Address : ')
    admin = Admin(name=name, email=email, address=address)

    admin.createAdmin(admin, bank)

    while True:
        print(f'\n-----Welcome {admin.name} as an Admin-----\n')
        print("1. View All Users")
        print("2. Delete User Account")
        print("3. View total bank balance")
        print("4. View total bank loan")
        print("5. Switch Loan Feature")
        print("6. Exit")

        choice = int(input('Enter your choice : '))
        if choice == 1:
            admin.view_users(bank)

        elif choice == 2:
            email = input("Enter email to delete: ")
            admin.remove_user(email, bank)
        
        elif choice == 3:
            admin.check_total_balance(bank)

        elif choice == 4:
            admin.check_total_loan(bank)

        elif choice == 5:
            decision = input("Enter decision (y / n): ")
            if(decision == 'y'):
                admin.loan_feature(True, bank)
            else:
                admin.loan_feature(False, bank)

        elif choice == 6:
            break
        else:
            print('Invalid Input')


while True:
    print('\n------Welcome Our Bank------\n')
    print('1. Customer')
    print('2. Admin')
    print('3. Exit')

    choice = int(input('Enter your choice : '))
    if choice == 1:
        customerLogin()

    elif choice == 2:
        adminMenu()

    elif choice == 3:
        break
    
    else:
        print('Invalid Input')
