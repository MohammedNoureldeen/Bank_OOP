from sqlalchemy.orm import Session
from src.models.account import Account, Transaction
from typing import List, Optional

class AccountRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_account(self, account: Account) -> Account:
        self.db.add(account)
        self.db.commit()
        self.db.refresh(account)
        return account

    def get_account(self, account_number: str) -> Optional[Account]:
        return self.db.query(Account).filter(Account.account_number == account_number).first()

    def get_all_accounts(self) -> List[Account]:
        return self.db.query(Account).all()

    def update_account(self, account: Account) -> Account:
        self.db.commit()
        self.db.refresh(account)
        return account

    def delete_account(self, account: Account) -> None:
        self.db.delete(account)
        self.db.commit()

    def create_transaction(self, transaction: Transaction) -> Transaction:
        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)
        return transaction

    def get_account_transactions(self, account_id: int) -> List[Transaction]:
        return self.db.query(Transaction).filter(Transaction.account_id == account_id).all() 