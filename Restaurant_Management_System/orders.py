import csv
import os
import uuid
from menu import MENU_FILE,BASE_DIR

ORDER_FILE = os.path.join(BASE_DIR, 'data/orders.csv')

def create_order_file():

    if not os.path.exists(ORDER_FILE):
        with open(ORDER_FILE, 'w', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(['order_id','item_name','quantity','price','total'])

def place_order():

    menu_items = []

    with open(MENU_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            menu_items.append(row)

    item_id = input('Enter Item ID: ')

    selected = None

    for item in menu_items:
        if item['item_id'] == item_id:
            selected = item
            break

    if not selected:
        print('\nItem Not Found !')
        return
    
    quantity = int(input('Enter Quantity: '))

    price = float(selected['price'])

    total = quantity * price

    order_id = 'O' + str(uuid.uuid4())[:5]

    with open(ORDER_FILE, 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                order_id,
                selected['item_name'],
                quantity,
                price,
                total
            ]
        )

    print('Order Placed Successfully.')
    print('Order ID: ',order_id)
    