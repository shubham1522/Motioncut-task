import json
import os

class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return []

    def save_expenses(self):
        with open(self.filename, "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, description, category):
        expense = {
            "amount": amount,
            "description": description,
            "category": category,
            "date": "2025-02-23"  # Ideally, use datetime module for real dates
        }
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self):
        for expense in self.expenses:
            print(f"Amount: {expense['amount']} | Description: {expense['description']} | Category: {expense['category']}")

    def get_monthly_summary(self, month):
        total = sum(expense['amount'] for expense in self.expenses if expense['date'].startswith(month))
        return total

    def get_category_summary(self, category):
        total = sum(expense['amount'] for expense in self.expenses if expense['category'] == category)
        return total


# Main Loop
tracker = ExpenseTracker()

while True:
    print("\nExpense Tracker Menu")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Monthly Summary")
    print("4. View Category Summary")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        category = input("Enter category: ")
        tracker.add_expense(amount, description, category)
    elif choice == "2":
        tracker.view_expenses()
    elif choice == "3":
        month = input("Enter month (YYYY-MM): ")
        print(f"Total for {month}: ${tracker.get_monthly_summary(month)}")
    elif choice == "4":
        category = input("Enter category: ")
        print(f"Total for {category}: ${tracker.get_category_summary(category)}")
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
