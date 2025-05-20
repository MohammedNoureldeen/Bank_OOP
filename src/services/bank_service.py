from src.database.account_repository import AccountRepository
from src.models.account import Account, Transaction
from datetime import datetime
import uuid
from typing import Optional, List

class BankService:
    MINIMUM_BALANCE = 100
    BANK_NAME = "EGYBBS"

    def __init__(self, repository: AccountRepository):
        self.repository = repository

    def create_account(self, name: str, balance: float, gender: str, account_type: str = "savings") -> Account:
        if balance < self.MINIMUM_BALANCE:
            raise ValueError(f"Initial balance must be at least {self.MINIMUM_BALANCE} EGP")

        # Generate unique account number using timestamp and UUID
        unique_id = str(uuid.uuid4())[:8]
        account_number = f"{self.BANK_NAME}-{datetime.now().strftime('%Y%m%d%H%M%S')}-{unique_id}"

        account = Account(
            name=name,
            balance=balance,
            gender=gender,
            account_type=account_type,
            account_number=account_number
        )
        return self.repository.create_account(account)

    def deposit(self, account_number: str, amount: float) -> Optional[Account]:
        account = self.repository.get_account(account_number)
        if not account or not account.is_active:
            raise ValueError("Account not found or inactive")

        if amount <= 0:
            raise ValueError("Amount must be greater than 0")

        account.balance += amount
        transaction = Transaction(
            account_id=account.id,
            transaction_type="deposit",
            amount=amount,
            description=f"Deposit of {amount} EGP"
        )
        self.repository.create_transaction(transaction)
        return self.repository.update_account(account)

    def withdraw(self, account_number: str, amount: float) -> Optional[Account]:
        account = self.repository.get_account(account_number)
        if not account or not account.is_active:
            raise ValueError("Account not found or inactive")

        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        if amount > account.balance:
            raise ValueError("Insufficient balance")

        account.balance -= amount
        transaction = Transaction(
            account_id=account.id,
            transaction_type="withdrawal",
            amount=amount,
            description=f"Withdrawal of {amount} EGP"
        )
        self.repository.create_transaction(transaction)
        return self.repository.update_account(account)

    def transfer(self, from_account_number: str, to_account_number: str, amount: float) -> tuple[Optional[Account], Optional[Account]]:
        from_account = self.repository.get_account(from_account_number)
        to_account = self.repository.get_account(to_account_number)

        if not from_account or not to_account:
            raise ValueError("One or both accounts not found")
        if not from_account.is_active or not to_account.is_active:
            raise ValueError("One or both accounts are inactive")
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        if amount > from_account.balance:
            raise ValueError("Insufficient balance")

        # Perform transfer
        from_account.balance -= amount
        to_account.balance += amount

        # Create transactions
        from_transaction = Transaction(
            account_id=from_account.id,
            transaction_type="transfer_out",
            amount=amount,
            description=f"Transfer to {to_account.name}: {amount} EGP"
        )
        to_transaction = Transaction(
            account_id=to_account.id,
            transaction_type="transfer_in",
            amount=amount,
            description=f"Transfer from {from_account.name}: {amount} EGP"
        )

        self.repository.create_transaction(from_transaction)
        self.repository.create_transaction(to_transaction)
        
        return (
            self.repository.update_account(from_account),
            self.repository.update_account(to_account)
        )

    def get_account_transactions(self, account_number: str) -> List[Transaction]:
        account = self.repository.get_account(account_number)
        if not account:
            raise ValueError("Account not found")
        return self.repository.get_account_transactions(account.id) 