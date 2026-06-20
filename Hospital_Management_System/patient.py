import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATIENT_FILE = os.path.join(BASE_DIR, 'data/patient.csv')

HEADER = [
    'patient_id',
    'name',
    'age',
    'gender',
    'phone'
]

def create_patient_file():

    DATA_DIR = os.path.join(BASE_DIR, 'data')
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(PATIENT_FILE):

        with open(PATIENT_FILE, 'w', newline='') as file:

            writer = csv.writer(file)
            writer.writerow(HEADER)

