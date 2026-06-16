import csv
from datetime import datetime

expenses = []

def add_expense():

    date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    category = input('Enter category: ')
    amount = float(input('Enter amount: '))

    expense = {
        'Date': date,
        'Category': category,
        'Amount': amount
    }

    expenses.append(expense)

    print('Expense added...')

def view_expenses():

    if len(expenses) ==0:
        print('\nExpense not found !')
        return
    
    for expense in expenses:

        print('\nDate: ',expense['Date'])
        print('Category: ',expense['Category'])
        print('Amount: ',expense['Amount'])
        print('-' *20)

def monthly_report():

    total = 0

    for expense in expenses:
          
        total += expense['Amount']

    print('\nTotal monthly Expense: ₹',total)

def category_report():
    
    if len(expenses)==0:
        print('\nNo datas found !')
        return

    category_total = {}

    for expense in expenses:

        category = expense['Category']

        if category not in category_total:

            category_total[category] = 0

        category_total[category] += expense['Amount']

    print('\nCategory wise spending:-')

    for category, amount in category_total.items():

        print(category,':',amount) 

def export_csv():

    with open('expenses.csv', 'w', newline='') as file:

        writer = csv.writer(file)

        writer.writerow(['Date','Category','Amount'])

        for expense in expenses:

            writer.writerow([
                expense['Date'],
                expense['Category'],
                expense['Amount']
            ])

    print('Exported successfully !')

while True:

    print("\n===== Expense Tracker =====\n")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Monthly Report")
    print("4. Category Report")
    print("5. Export CSV")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        monthly_report()

    elif choice == "4":
        category_report()

    elif choice == "5":
        export_csv()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")