class BankAccount:
    def __init__(self, name, balance=0):

        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        
        if amount > 0:
            self.balance += amount
            print(f"KES {amount} deposited successfully.")
        else:
            print("Invalid deposit amount!")
    
    def withdraw(self, amount):
        
        if amount > self.balance:
            print("Error: Insufficient funds!")
        elif amount <= 0:
            print("Invalid withdrawal amount!")
        else:
            self.balance -= amount
            print(f"KES {amount} withdrawn successfully.")
    
    def check_balance(self):
        """Print the current balance of the account."""
        print(f"Your current balance is: KES {self.balance}")
    

def main():
    
    print("Welcome to Python ATM!")
    
    # Account creation
    name = input("Please enter your name: ")
    while True:
        try:
            initial_balance = float(input("Please enter your initial balance: "))
            if initial_balance < 0:
                print("Initial balance cannot be negative!")
                continue
            break
        except ValueError:
            print("Please enter a valid number for the balance.")
    
    account = BankAccount(name, initial_balance)
    print("Account created successfully!\n")
    
    # Main menu loop
    while True:
        print("\nATM Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice, please enter a number between 1 and 4.")
            continue
        
        if choice == 1:
            # Deposit money
            try:
                deposit_amount = float(input("Enter deposit amount: "))
                account.deposit(deposit_amount)
            except ValueError:
                print("Invalid input! Please enter a valid amount.")
        
        elif choice == 2:
            # Withdraw money
            try:
                withdrawal_amount = float(input("Enter withdrawal amount: "))
                account.withdraw(withdrawal_amount)
            except ValueError:
                print("Invalid input! Please enter a valid amount.")
        
        elif choice == 3:
            # Check balance
            account.check_balance()
        
        elif choice == 4:
            # Exit the system
            print(f"Thank you for using Python ATM, {account.name}. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    main()
