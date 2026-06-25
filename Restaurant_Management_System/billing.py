import csv
from orders import ORDER_FILE

def generate_bill():

    order_id = input('Enter Order ID: ')
    
    found = False

    with open(ORDER_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:

            if row['order_id'] == order_id:
                found = True

                print('\n----------BILL------------')
                
                print('Order ID: ',row['order_id'])
                print('Item    : ',row['item_name'])
                print('Quantity: ',row['quantity'])
                print('Price   : ',row['price'])
                print('Total   : ₹',row['total'])

                break
    
    if not found:
        print('Order Not Found !')