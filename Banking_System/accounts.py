import csv
import os
import uuid

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILE_NAME = os.path.join(BASE_DIR, 'accounts.csv')

def initialize_file():

    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(
                [
                    'account_no',
                    'name',
                    'phone',
                    'balance'
                ]
            )

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
