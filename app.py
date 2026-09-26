import csv

# Read CSV file
with open("csv2.csv", "r") as file:
    data = csv.reader(file)

    header = next(data)
    transactions = list(data)


# Total Income & Expenses

total_income = 0
total_expenses = 0
balance = 0
saving_rate = 0

for trans in transactions:
    if trans[2] == "Income":
        total_income = total_income + int(trans[4])

    elif trans[2] == "Expense":
        total_expenses = total_expenses + int(trans[4])


balance = total_income - total_expenses


if total_income > 0:
    saving_rate = (balance / total_income) * 100
else:
    saving_rate = 0


print("Total Income:", total_income)
print("Total Expenses:", total_expenses)
print("Balance:", balance)
print("Saving Rate:", saving_rate)


# Category-wise Expenses

category_expenses = {}

for trans in transactions:
    if trans[2] == "Expense":

        category = trans[1]
        amount = int(trans[4])

        if category in category_expenses:
            category_expenses[category] = category_expenses[category] + amount
        else:
            category_expenses[category] = amount


print("Category-wise Expenses:", category_expenses)


# Highest Expense

if category_expenses:
    highest_expense = max(category_expenses, key=category_expenses.get)
    highest_expense_amount = category_expenses[highest_expense]

    print("Highest Expense:", highest_expense)
    print("Highest Expense Amount:", highest_expense_amount)
else:
    print("No expenses found.")


# Monthly Expenses

monthly_expenses = {}

for trans in transactions:
    if trans[2] == "Expense":

        date = trans[0]
        amount = int(trans[4])

        # Get year-month, e.g. 2026-01
        month = date[:7]

        if month in monthly_expenses:
            monthly_expenses[month] = monthly_expenses[month] + amount
        else:
            monthly_expenses[month] = amount


print("Monthly Expenses:", monthly_expenses)
