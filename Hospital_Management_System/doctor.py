import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
DOCTOR_FILE = os.path.join(BASE_DIR, 'data/doctor.csv')

HEADER = [
    'doctor_id',
    'name',
    'specialisation',
    'phone'
]

def create_file():

    os.makedirs(DATA_DIR, exist_ok= True)

    if not os.path.exists(DOCTOR_FILE):
        with open(DOCTOR_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(HEADER)
