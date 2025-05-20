class Bank:
    account_count = 0  # class level attribute
    Bank_name = "EGYBBS"
    MINIMUM_BALANCE = 100  # minimum balance requirement

    @classmethod
    def get_total_accounts(cls):
        return f"Total bank accounts: {cls.account_count}"

    @staticmethod
    def currency_changer(amount, rate):
        return amount * rate

    def __init__(self, name, balance, gender, account_type="savings"):
        if balance < self.MINIMUM_BALANCE:
            raise ValueError(f"Initial balance must be at least {self.MINIMUM_BALANCE} EGP")
        
        self.name = name
        self.__balance = balance
        self.gender = gender
        self.account_type = account_type
        self.transaction_history = []
        Bank.account_count += 1
        self.account_number = f"{Bank.Bank_name}-{Bank.account_count:04d}"
        self.__is_active = True

    def get_balance(self):
        if not self.__is_active:
            return "Account is inactive"
        return f"{self.name} ({self.gender}) - Account: {self.account_number} - Balance: {self.__balance} EGP"

    def deposit(self, amount):
        if not self.__is_active:
            return "ERROR: Account is inactive"
        if amount > 0:
            self.__balance += amount
            self.transaction_history.append(f"Deposit: +{amount} EGP")
            return f"{amount} EGP deposited successfully."
        return "ERROR: Amount must be over 0 EGP."

    def withdraw(self, amount):
        if not self.__is_active:
            return "ERROR: Account is inactive"
        if amount <= 0:
            return "ERROR: Amount must be over 0 EGP."
        if amount <= self.__balance:
            self.__balance -= amount
            self.transaction_history.append(f"Withdrawal: -{amount} EGP")
            return f"Withdrawn {amount} EGP successfully."
        return "ERROR: Not enough balance."

    def get_transaction_history(self):
        if not self.__is_active:
            return "ERROR: Account is inactive"
        return self.transaction_history

    def deactivate_account(self):
        if self.__balance > 0:
            return "ERROR: Cannot deactivate account with remaining balance"
        self.__is_active = False
        return "Account deactivated successfully"

    def activate_account(self):
        if self.__is_active:
            return "Account is already active"
        self.__is_active = True
        return "Account activated successfully"

    def transfer(self, recipient, amount):
        if not self.__is_active or not recipient.__is_active:
            return "ERROR: One or both accounts are inactive"
        if amount <= 0:
            return "ERROR: Amount must be over 0 EGP."
        if self.__balance == recipient.__balance:
            return "ERORR Can not send to yourself"
        if amount <= self.__balance:
            self.__balance -= amount
            recipient.__balance += amount
            self.transaction_history.append(f"Transfer to {recipient.name}: -{amount} EGP")
            recipient.transaction_history.append(f"Transfer from {self.name}: +{amount} EGP")
            return f"Transferred {amount} EGP to {recipient.name} successfully."
        return "ERROR: Not enough balance for transfer."

# Example usage
if __name__ == "__main__":
    try:
        # Create accounts
        acc1 = Bank("Ali", 5000, "Male", "savings")
        acc2 = Bank("Nora", 8000, "Female", "checking")
        
        # Display initial information
        print(Bank.get_total_accounts())
        print(f"Currency conversion: {Bank.currency_changer(100, 50.9)}")
        
        # Making  transactions
        print("\nAccount Operations:")
        print(acc1.get_balance())
        print(acc1.deposit(100))
        print(acc1.withdraw(2999))
        print(acc1.get_balance())
        
        # Transfer money
        print("\nTransfer Operations:")
        print(acc1.transfer(acc2, 500))
        print(acc1.get_balance())
        print(acc2.get_balance())
        print(acc1.transfer(acc1,200))
        
        # Show transaction history
        print("\nTransaction History:")
        print("Ali's transactions:", acc1.get_transaction_history())
        print("Nora's transactions:", acc2.get_transaction_history())
        
    except ValueError as e:
        print(f"Error: {e}")