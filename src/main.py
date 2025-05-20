from src.config.database_config import Base, engine, SessionLocal
from src.database.account_repository import AccountRepository
from src.services.bank_service import BankService

def init_db():
    # Create all tables
    Base.metadata.create_all(bind=engine)

def main():
    # Initialize database
    init_db()
    
    # Create database session
    db = SessionLocal()
    repository = AccountRepository(db)
    bank_service = BankService(repository)

    try:
        # Create two accounts
        print("\n=== Creating Accounts ===")
        account1 = bank_service.create_account("John Doe", 1000, "Male", "savings")
        print(f"Created account for {account1.name}: {account1.account_number}")
        
        account2 = bank_service.create_account("Jane Smith", 2000, "Female", "checking")
        print(f"Created account for {account2.name}: {account2.account_number}")

        # Perform some operations
        print("\n=== Performing Operations ===")
        
        # Deposit
        print("\nDepositing 500 to John's account...")
        updated_account = bank_service.deposit(account1.account_number, 500)
        print(f"New balance: {updated_account.balance} EGP")

        # Withdraw
        print("\nWithdrawing 200 from John's account...")
        updated_account = bank_service.withdraw(account1.account_number, 200)
        print(f"New balance: {updated_account.balance} EGP")

        # Transfer
        print("\nTransferring 300 from John to Jane...")
        from_acc, to_acc = bank_service.transfer(account1.account_number, account2.account_number, 300)
        print(f"John's new balance: {from_acc.balance} EGP")
        print(f"Jane's new balance: {to_acc.balance} EGP")

        # Get transaction history
        print("\n=== Transaction History ===")
        print("\nJohn's transactions:")
        for transaction in bank_service.get_account_transactions(account1.account_number):
            print(f"- {transaction.description} ({transaction.created_at})")

        print("\nJane's transactions:")
        for transaction in bank_service.get_account_transactions(account2.account_number):
            print(f"- {transaction.description} ({transaction.created_at})")

    except ValueError as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main() 