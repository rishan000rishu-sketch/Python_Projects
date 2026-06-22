import os
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR  = os.path.join(BASE_DIR, 'data')
PATIENT_FILE = os.path.join(BASE_DIR, 'data/patient.csv')
BILL_FILE = os.path.join(BASE_DIR, 'data/bills.csv')

HEADER = [
    "bill_id",
    "patient_id",
    "consultation_fee",
    "medicine_charge",
    "lab_charge",
    "total_amount"
]

def create_bill_file():

    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(BILL_FILE):
        with open(BILL_FILE, 'w', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(HEADER)

def patient_exists(patient_id):

    with open(PATIENT_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['patient_id'] == patient_id:
                return True
            
    return False
