from dataclasses import dataclass
from typing import List
import calendar
import datetime

@dataclass
class Expense:
    name: str
    category: str
    amount: float

def main():
    print("Finance tracker has been activated. 📑")
    expense_file_path = "expenses.csv"
    budget = 2000

    # Get user expenses
    expenses = get_user_expenses()

    # Write the expenses to file
    save_expenses_to_file(expenses, expense_file_path)

    # Read file and summarize expenses
    summarize_expenses(expense_file_path, budget)

def get_user_expenses() -> List[Expense]:
    print("💻 Getting your Expenses!")
    expenses = []
    expense_categories = [
        "🍕 Food",
        "🏫 School",
        "🚕 Transportation",
        "🎴 Needs",
        "💻 Wants"
    ]

    while True:
        expense_name = input("Enter expense name (or type 'done' to finish): ")
        if expense_name.lower() == 'done':
            break

        try:
            expense_amount = float(input("Enter expense amount: "))
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            continue

        selected_category = select_category(expense_categories)
        if selected_category:
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            expenses.append(new_expense)

    return expenses

def select_category(categories: List[str]) -> str:
    print("Select a category: ")
    for i, category_name in enumerate(categories):
        print(f"  {i + 1}. {category_name}")

    while True:
        try:
            selected_index = int(input(f"Enter a category number [1 - {len(categories)}]: ")) - 1
            if 0 <= selected_index < len(categories):
                return categories[selected_index]
            else:
                print("Please select a valid category.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def save_expenses_to_file(expenses: List[Expense], expense_file_path: str):
    print(f"🌌 Saving User Expenses to {expense_file_path}")
    with open(expense_file_path, "a", encoding='utf-8') as f:
        for expense in expenses:
            f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expenses(expense_file_path: str, budget: float):
    print("🎯 Summarizing User Expenses")
    expenses = read_expenses_from_file(expense_file_path)

    amount_by_category = {}
    for expense in expenses:
        amount_by_category[expense.category] = amount_by_category.get(expense.category, 0) + expense.amount

    print("Expenses By Category 📈:")
    for category, total in amount_by_category.items():
        print(f"  {category}: ₱{total:.2f}")

    total_spent = sum(expense.amount for expense in expenses)
    print(f"💵 Total Spent: ₱{total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"✅ Budget Remaining: ₱{remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    if remaining_days > 0:
        daily_budget = remaining_budget / remaining_days
        print(f"👉 Budget Per Day: ₱{daily_budget:.2f}")
    else:
        print("📅 No remaining days in the month to calculate daily budget.")

def read_expenses_from_file(expense_file_path: str) -> List[Expense]:
    expenses = []
    try:
        with open(expense_file_path, "r", encoding='utf-8') as f:
            for line in f:
                if line.strip():  # Check if the line is not empty
                    expense_name, expense_amount, expense_category = line.strip().split(",")
                    expenses.append(Expense(
                        name=expense_name,
                        amount=float(expense_amount),
                        category=expense_category,
                    ))
    except FileNotFoundError:
        print(f"File {expense_file_path} not found. Starting with an empty expense list.")
    except ValueError as e:  # Fixed typo here
        print(f"Error reading file: {e}")
    return expenses

if __name__ == '__main__':
    main()