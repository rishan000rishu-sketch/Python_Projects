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

def patient_exists(patient_id):

    with open(PATIENT_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:

            if row['patient_id'] == patient_id:
                return True
            
    return False

def add_patient():
    patient_id  = input('Enter Patient_ID: ')

    if patient_exists(patient_id):
        print('Patient Already Exists !')
        return
    
    name = input('Enter Patient Name: ')
    age = int(input('Enter Patient Age: '))
    gender  = input('Enter Gender (male/female/others): ')
    phone = int(input('Enter Phone No: '))

    with open(PATIENT_FILE, 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(HEADER)
        writer.writerow([
            patient_id,
            name,
            age,
            gender,
            phone
        ])

    print('Patient Added Successfully.')
