import csv
import os
import uuid

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILE_NAME = os.path.join(BASE_DIR, 'accounts.csv')

HEADER = [
    'account_no',
    'name',
    'phone',
    'balance'
]

def initialize_file():

    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(HEADER)

def create_account():

    name = input('Enter Account Holder Name: ')

    phone = int(input('Enter Holder Phone No: '))

    account_no = 'ACC' + str(uuid.uuid4())[:6]

    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow([
            account_no,
            name,
            phone,
            0
        ])

    print('\nAccount Created Successfully.')
    print(f'Account Number: {account_no}')

def view_accounts():

    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)

        print('\n------Account List------')

        for row in reader:
            print(row)

def get_account(account_no):

    with open(FILE_NAME, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:

            if row['account_no'] == account_no:
                return row
            
    return None

def update_balance(account_no, new_balance):

    rows = []

    with open(FILE_NAME, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            
            if row['account_no'] == account_no:
                row['balance'] = str(new_balance)
            
            rows.append(row)

    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=HEADER)

        writer.writeheader()
        writer.writerows(rows)
