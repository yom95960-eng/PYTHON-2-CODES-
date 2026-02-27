class BankAccount:
    def __init__(self, account_no, balance=0):
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Amount withdrawn: {amount}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

if __name__ == "__main__":
    account = BankAccount(account_no=101, balance=1000)

    account.check_balance()
    account.deposit(500)
    account.withdraw(300)
    account.check_balance()