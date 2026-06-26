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
