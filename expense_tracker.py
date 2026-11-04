expenses = []

def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter category: ")

    expenses.append({
        "amount": amount,
        "category": category
    })

    print("Expense added successfully!")

def view_expenses():
    total = 0

    print("\nYour Expenses:")

    for expense in expenses:
        print(expense["category"], "-", expense["amount"])
        total += expense["amount"]

    print("Total Expense:", total)

while True:
    print("\n--- EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
