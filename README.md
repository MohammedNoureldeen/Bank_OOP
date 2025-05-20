# EGYBBS Banking System

A modern, object-oriented banking system with a graphical user interface (GUI) built using Tkinter and a persistent SQLite database backend using SQLAlchemy.

## Features
- Create, deposit, withdraw, and transfer between accounts
- Transaction history for each account
- Data is stored in a database (not lost when you close the app)
- Clean, modern UI
- Follows best practices: OOP, service/repository patterns, and separation of concerns

## Folder Structure
```
Bank_OOP/
├── bank_ui.py           # Main GUI application
├── bank.db              # SQLite database file (auto-created)
├── requirements.txt     # Python dependencies
├── src/                 # Source code for backend logic
│   ├── config/
│   │   └── database_config.py
│   ├── database/
│   │   └── account_repository.py
│   ├── models/
│   │   └── account.py
│   └── services/
│       └── bank_service.py
└── README.md            # This file
```

## Setup Instructions

### 1. Clone the Repository
```
git clone <https://github.com/MohammedNoureldeen/Bank_OOP>
cd Bank_OOP
```

### 2. Install Dependencies
Make sure you have Python 3.8–3.12 installed (not 3.13) >>HAAAA.

```
pip install -r requirements.txt
```

### 3. Run the Application
```
python bank_ui.py
```

- The database (`bank.db`) will be created automatically on first run.
- All account and transaction data is saved in the database.

## How to Use
- **Create Account:** Fill in the details and click "Create Account".
- **Deposit/Withdraw:** Select an account, enter an amount, and click the respective button.
- **Transfer:** Select an account, choose a recipient, enter an amount, and click "Transfer".
- **Check Balance:** Select an account and click "Check Balance".
- **Transaction History:** Select an account to view its transaction history.

## Notes
- The UI and backend are fully decoupled: you can extend the backend or swap the UI easily.
- All business logic and data access are in the `src/` folder.
- The app is ready for further extension (e.g., user authentication, more account types, etc.).

## Troubleshooting
- If you get errors about missing modules, double-check you ran `pip install -r requirements.txt`.
- If you use Python 3.13, you may encounter SQLAlchemy compatibility issues. Use Python 3.8–3.12.

## License
MIT (or specify your license here) 