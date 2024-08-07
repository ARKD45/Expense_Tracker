import json
from datetime import datetime

# Define the file to store expenses
EXPENSE_FILE = 'expenses.json'

# Load expenses from the file
def load_expenses():
    try:
        with open(EXPENSE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save expenses to the file
def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses, amount, description, category):
    date_str = datetime.now().strftime('%Y-%m-%d')
    if date_str not in expenses:
        expenses[date_str] = []
    expenses[date_str].append({'amount': amount, 'description': description, 'category': category})
    save_expenses(expenses)
    print("Expense added successfully.")

# View summary of monthly expenses
def view_monthly_summary(expenses):
    monthly_summary = {}
    for date, daily_expenses in expenses.items():
        month = date[:7]
        if month not in monthly_summary:
            monthly_summary[month] = 0
        for expense in daily_expenses:
            monthly_summary[month] += expense['amount']
    for month, total in monthly_summary.items():
        print(f'{month}: ${total:.2f}')

# View category-wise expenditure
def view_category_summary(expenses):
    category_summary = {}
    for daily_expenses in expenses.values():
        for expense in daily_expenses:
            category = expense['category']
            if category not in category_summary:
                category_summary[category] = 0
            category_summary[category] += expense['amount']
    for category, total in category_summary.items():
        print(f'{category}: ${total:.2f}')

# Main function to run the Expense Tracker
def main():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category Summary")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                description = input("Enter description: ")
                category = input("Enter category: ")
                add_expense(expenses, amount, description, category)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == '2':
            view_monthly_summary(expenses)
        elif choice == '3':
            view_category_summary(expenses)
        elif choice == '4':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
