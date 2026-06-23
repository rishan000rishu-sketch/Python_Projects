import csv 
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USER_FILE = os.path.join(BASE_DIR, 'data/users.csv')

def login():

    username = input('Enter Username: ')
    password = input('Enter Password: ')

    try:
        with open(USER_FILE, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:

                if (
                    row['username'] == username and
                    row['password'] == password
                ):
                    
                    return row
                
    except FileNotFoundError:
        print('Users File Not Found !')
            
    return None
