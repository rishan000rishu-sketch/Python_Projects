import csv
from orders import ORDER_FILE

def sales_report():

    total_sales = 0
    total_orders = 0

    with open(ORDER_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:

            total_orders += 1
            total_sales += float(row['total'])

    print('\n-------SALES REPORT-------')

    print('Total Orders: ',total_orders)
    print('Total Sales : ₹',total_sales)
    