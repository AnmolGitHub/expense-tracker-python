expenses = []
summary = {}

def add_expense(expenses):

    amount = float(input("Enter Amount: "))
    category = input("Enter Category: ")
    date = input("Enter Date: ")

    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)

    print("Expenses Added Successfully!")


def view_expenses(expenses):

    if not expenses:
        print("No expenses found!")
        return

    print("Expenses List:")

    for expense in expenses:
        print(
            f"amount: {expense['amount']}, "
            f"category: {expense['category']}, "
            f"date: {expense['date']}"
        )
def monthly_summary(expenses):
    month = input("Enter Month(YYYY-MM): ")
    total = 0
    for expense in expenses:
        if expense["date"].startswith(month):
            total += expense["amount"]
    print(f"Total Expenses for {month}: {total}")

while True:

    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Monthly Summary")
    print("4. Category Summary")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Invalid Input")
        continue

    if choice == 1:
        add_expense(expenses)
    elif choice == 2:
        view_expenses(expenses)
    elif choice == 3:
        monthly_summary(expenses)
    elif choice == 5:
        print("Bye!")
        break