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

def appoinment_exists(appoinment_id):

    with open(APPOINMENT_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['appoinment_id'] == appoinment_id:
                return True
            
    return False

def patient_exists(patient_id):

    with open(PATIENT_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['patient_id'] == patient_id:
                return True
            
    return False

def doctor_exists(doctor_id):

    with open(DOCTOR_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['doctor_id'] == doctor_id:
                return True
            
    return False
