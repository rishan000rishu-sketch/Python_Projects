import os
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, 'data')
DOCTOR_FILE = os.path.join(BASE_DIR, 'data/doctor.csv')
PATIENT_FILE = os.path.join(BASE_DIR, 'data/patient.csv')
APPOINMENT_FILE = os.path.join(BASE_DIR, 'data/appoinment.csv')


HEADER = [
    'appoinment_id',
    'doctor_id',
    'patient_id',
    'appoinment_date'
]

def create_file():

    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(APPOINMENT_FILE):

        with open(APPOINMENT_FILE, 'w', newline='') as file:
            
            writer = csv.writer(file)
            writer.writerow(HEADER)
