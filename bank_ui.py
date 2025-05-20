import tkinter as tk
from tkinter import ttk, messagebox
from OOP import Bank
import tkinter.font as tkfont

class BankUI:
    def __init__(self, root):
        self.root = root
        self.root.title("EGYBBS Banking System")
        self.root.geometry("1000x700")
        self.accounts = {}  # Dictionary to store accounts
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure("Modern.TFrame", background="#f0f0f0")
        self.style.configure("Modern.TLabel", background="#f0f0f0", font=("Helvetica", 10))
        self.style.configure("Modern.TButton", font=("Helvetica", 10, "bold"))
        self.style.configure("Title.TLabel", font=("Helvetica", 16, "bold"), background="#f0f0f0")
        
        # Create main frame with padding
        self.main_frame = ttk.Frame(self.root, style="Modern.TFrame", padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Add title
        title_label = ttk.Label(self.main_frame, text="EGYBBS Banking System", style="Title.TLabel")
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Create account creation section
        self.create_account_section()
        
        # Create account operations section
        self.create_operations_section()
        
        # Create transaction history section
        self.create_history_section()

    def create_account_section(self):
        # Account Creation Frame
        create_frame = ttk.LabelFrame(self.main_frame, text="Create New Account", padding="15")
        create_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10, padx=5)
        
        # Name
        ttk.Label(create_frame, text="Name:", style="Modern.TLabel").grid(row=0, column=0, padx=10, pady=5)
        self.name_var = tk.StringVar()
        ttk.Entry(create_frame, textvariable=self.name_var, width=20).grid(row=0, column=1, padx=10, pady=5)
        
        # Balance
        ttk.Label(create_frame, text="Initial Balance:", style="Modern.TLabel").grid(row=0, column=2, padx=10, pady=5)
        self.balance_var = tk.StringVar()
        ttk.Entry(create_frame, textvariable=self.balance_var, width=20).grid(row=0, column=3, padx=10, pady=5)
        
        # Gender
        ttk.Label(create_frame, text="Gender:", style="Modern.TLabel").grid(row=1, column=0, padx=10, pady=5)
        self.gender_var = tk.StringVar(value="Male")
        gender_frame = ttk.Frame(create_frame)
        gender_frame.grid(row=1, column=1, columnspan=2, sticky=tk.W)
        ttk.Radiobutton(gender_frame, text="Male", variable=self.gender_var, value="Male").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(gender_frame, text="Female", variable=self.gender_var, value="Female").pack(side=tk.LEFT, padx=5)
        
        # Account Type
        ttk.Label(create_frame, text="Account Type:", style="Modern.TLabel").grid(row=1, column=2, padx=10, pady=5)
        self.account_type_var = tk.StringVar(value="savings")
        ttk.Combobox(create_frame, textvariable=self.account_type_var, 
                    values=["savings", "checking"], width=17).grid(row=1, column=3, padx=10, pady=5)
        
        # Create Account Button
        create_btn = ttk.Button(create_frame, text="Create Account", 
                              command=self.create_account, style="Modern.TButton")
        create_btn.grid(row=2, column=0, columnspan=4, pady=15)

    def create_operations_section(self):
        # Operations Frame
        ops_frame = ttk.LabelFrame(self.main_frame, text="Account Operations", padding="15")
        ops_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10, padx=5)
        
        # Account Selection
        ttk.Label(ops_frame, text="Select Account:", style="Modern.TLabel").grid(row=0, column=0, padx=10, pady=5)
        self.account_var = tk.StringVar()
        self.account_combo = ttk.Combobox(ops_frame, textvariable=self.account_var, width=20)
        self.account_combo.grid(row=0, column=1, padx=10, pady=5)
        
        # Amount
        ttk.Label(ops_frame, text="Amount:", style="Modern.TLabel").grid(row=0, column=2, padx=10, pady=5)
        self.amount_var = tk.StringVar()
        ttk.Entry(ops_frame, textvariable=self.amount_var, width=20).grid(row=0, column=3, padx=10, pady=5)
        
        # Operation Buttons Frame
        btn_frame = ttk.Frame(ops_frame)
        btn_frame.grid(row=1, column=0, columnspan=4, pady=10)
        
        ttk.Button(btn_frame, text="Deposit", command=self.deposit, style="Modern.TButton").pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Withdraw", command=self.withdraw, style="Modern.TButton").pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Check Balance", command=self.check_balance, style="Modern.TButton").pack(side=tk.LEFT, padx=5)
        
        # Transfer Section
        transfer_frame = ttk.Frame(ops_frame)
        transfer_frame.grid(row=2, column=0, columnspan=4, pady=10)
        
        ttk.Label(transfer_frame, text="Transfer To:", style="Modern.TLabel").pack(side=tk.LEFT, padx=5)
        self.transfer_var = tk.StringVar()
        self.transfer_combo = ttk.Combobox(transfer_frame, textvariable=self.transfer_var, width=20)
        self.transfer_combo.pack(side=tk.LEFT, padx=5)
        ttk.Button(transfer_frame, text="Transfer", command=self.transfer, style="Modern.TButton").pack(side=tk.LEFT, padx=5)

    def create_history_section(self):
        # History 
        history_frame = ttk.LabelFrame(self.main_frame, text="Transaction History", padding="15")
        history_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10, padx=5)
        
        # Transaction List with custom font
        custom_font = tkfont.Font(family="Helvetica", size=10)
        self.history_text = tk.Text(history_frame, height=10, width=80, font=custom_font)
        self.history_text.grid(row=0, column=0, padx=5, pady=5)
        
        # Scrollwl
        scrollbar = ttk.Scrollbar(history_frame, orient=tk.VERTICAL, command=self.history_text.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.history_text['yscrollcommand'] = scrollbar.set

    def create_account(self):
        try:
            name = self.name_var.get()
            balance = float(self.balance_var.get())
            gender = self.gender_var.get()
            account_type = self.account_type_var.get()
            
            if not name:
                messagebox.showerror("Error", "Please enter a name")
                return
                
            account = Bank(name, balance, gender, account_type)
            self.accounts[account.account_number] = account
            
            # Update account selection dropdowns
            self.update_account_lists()
            
            messagebox.showinfo("Success", f"Account created successfully!\nAccount Number: {account.account_number}")
            
            # Clear input fields
            self.name_var.set("")
            self.balance_var.set("")
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_account_lists(self):
        account_numbers = list(self.accounts.keys())
        self.account_combo['values'] = account_numbers
        self.transfer_combo['values'] = account_numbers

    def get_selected_account(self):
        account_number = self.account_var.get()
        if not account_number:
            messagebox.showerror("Error", "Please select an account")
            return None
        return self.accounts.get(account_number)

    def deposit(self):
        account = self.get_selected_account()
        if not account:
            return
            
        try:
            amount = float(self.amount_var.get())
            result = account.deposit(amount)
            messagebox.showinfo("Success", result)
            self.update_history()
            self.amount_var.set("")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")

    def withdraw(self):
        account = self.get_selected_account()
        if not account:
            return
            
        try:
            amount = float(self.amount_var.get())
            result = account.withdraw(amount)
            messagebox.showinfo("Success", result)
            self.update_history()
            self.amount_var.set("")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")

    def check_balance(self):
        account = self.get_selected_account()
        if not account:
            return
            
        messagebox.showinfo("Balance", account.get_balance())

    def transfer(self):
        from_account = self.get_selected_account()
        if not from_account:
            return
            
        to_account_number = self.transfer_var.get()
        if not to_account_number:
            messagebox.showerror("Error", "Please select a recipient account")
            return
            
        to_account = self.accounts.get(to_account_number)
        if not to_account:
            messagebox.showerror("Error", "Recipient account not found")
            return
            
        try:
            amount = float(self.amount_var.get())
            result = from_account.transfer(to_account, amount)
            messagebox.showinfo("Success", result)
            self.update_history()
            self.amount_var.set("")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")

    def update_history(self):
        account = self.get_selected_account()
        if not account:
            return
            
        self.history_text.delete(1.0, tk.END)
        history = account.get_transaction_history()
        for transaction in history:
            self.history_text.insert(tk.END, transaction + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankUI(root)
    root.mainloop() 