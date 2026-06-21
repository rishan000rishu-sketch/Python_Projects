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
           
def doctor_exists(doctor_id):

    with open(DOCTOR_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['doctor_id'] == doctor_id:
                return True            
 
    return False

def add_doctor():

    doctor_id = input('Enter Doctor_ID: ')

    if doctor_exists(doctor_id):
        print('\nDoctor_ID Already Existed !')
        return
    
    name = input('Enter Doctor Name: ')
    specialisation = input('Enter Specialisation: ')
    phone = int(input('Enter Phone No: '))

    with open(DOCTOR_FILE, 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow([
            doctor_id,
            name,
            specialisation,
            phone
        ])

    print('Doctor Added Successfully.')

def view_doctors():

    with open(DOCTOR_FILE, 'r') as file:
        reader = csv.DictReader(file)

        print('\n--------DOCTORS--------')

        for row in reader:

            print(
                f'{row['doctor_id']} | '
                f'{row['name']} | '
                f'{row['specialisation']} | '
                f'{row['phone']} | '
            )

def search_doctor():

    doctor_id = input('Enter Doctor_ID: ')

    with open(DOCTOR_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['doctor_id'] == doctor_id:
                
                print(
                f'{row['doctor_id']} | '
                f'{row['name']} | '
                f'{row['specialisation']} | '
                f'{row['phone']} | '
            )
                