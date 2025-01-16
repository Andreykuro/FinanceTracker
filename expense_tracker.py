from expense import expense


def main():
    print(f"This Expense Tracker has been brought to life!")

    #this is the input (expenses)
    get_user_expenses()

    # Write the expenses file
    save_expenses_to_file()

    # Read file and summarize expenses
    summarize_expenses()

def get_user_expenses():
    print(f"💻 Getting your Expenses!")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    print(f"You've entered {expense_name}, {expense_amount}")

    expense_category = [
        "🍕 Food",
        "🏫 School",
        "🚕 Transportation",
        "🎴 Needs",
        "💻 Wants"
    ]

    while True:
        print("Select a category: ")
        for i, expense_category in enumerate(expense_category):
            print(f"    {i+1}. {expense_category}")
            break


def save_expenses_to_file():
    print(f"Your expenses -- input here")

def summarize_expenses():
    print(f"Your expenses -- input here")


if __name__ == '__main__':
    main()