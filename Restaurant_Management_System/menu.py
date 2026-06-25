import csv
import os

BAS_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BAS_DIR, 'data')
MENU_FILE = os.path.join(BAS_DIR, 'data/menu.csv')

HEADER = [
    'item_id',
    'item_name',
    'price'
]

def item_exists(item_id):

    with open(MENU_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['item_id'] == item_id:
                return True
            
    return False
            
def add_item():

    os.makedirs(DATA_DIR, exist_ok= True)

    if not os.path.exists(MENU_FILE):
        with open(MENU_FILE, 'w', newline='') as file:
            writer =  csv.writer(file)

            writer.writerow(HEADER)

    item_id = input('Enter Item ID: ')

    if item_exists(item_id):
        print('\nItem ID Already Exists !')
        return

    item_name = input('Enter Item Name: ')
    price = input('Enter Price: ')
            
    if os.path.exists(MENU_FILE):
        with open(MENU_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
         
            writer.writerow(
                [
                    item_id,
                    item_name,
                    price
                ])
            
        print('\nItem Added Successfully.')

