import csv
import os
from accounts import get_account, update_balance
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRANSACTIOIN_FILE = os.path.join(BASE_DIR, 'transactions.csv')

HEADER = [
    "account_no",
    "type",
    "amount",
    "date_time"
]

def create_file():

    if not os.path.exists(TRANSACTIOIN_FILE):
        with open(TRANSACTIOIN_FILE, 'w', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(HEADER)

def save_transactions(account_no, trans_type, amount):

    with open(TRANSACTIOIN_FILE, 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                account_no,
                trans_type,
                amount,
                datetime.now()
            ]
        )

def deposit():

    account_no = input('Enter Account No: ')

    account = get_account(account_no)

    if not account:
        print('\nAccount Not Found !')
        return
    
    amount = float(input('Enter Deposit Amount: '))

    new_balance = float(account['balance']) + amount

    update_balance(account_no, new_balance)

    save_transactions(account_no, 'Deposit', amount)

    print('\nDeposit Completed Successfully.')
    
def withdraw():

    account_no = input('Enter Account No: ')

    account = get_account(account_no)

    if not account:
        print('\nAccount Not Found')
        return
    
    amount = float(input('Enter Withdrawal amount'))

    current_balance = float(account['balance'])

    if amount > current_balance:
        print('Insufficient Balance')
        return

    new_balance = float(account['balance']) - amount

    update_balance(account_no, new_balance)

    save_transactions(account_no, 'Withdraw', amount)

    print('\nCash Withdrawal Completed')
