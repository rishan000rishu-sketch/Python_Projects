import csv 
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(BASE_DIR, 'rooms.csv')

rooms = []

def add_rooms():

    load_room_data()

    room_no = int(input('Enter room no: '))

    for room in rooms:

        if room['Room no'] == room_no:
            
            print('Room already exists !')
            return

    room_type = input('Enter room type: (single/double/etc..) ')
    room_price = int(input('Enter room price: '))

    room = {
        'Room no':room_no,
        'Room type':room_type,
        'Room price':room_price
    }

    rooms.append(room)
    
    save_room_data()
    print('Room data saved..')

def view_rooms():

    load_room_data()

    for room in rooms:

        print('Room No: ',room['Room no'])
        print('Room Type: ',room['Room type'])
        print(f'Room Price: ,{room['Room price']}\n')

def edit_rooms():

    load_room_data()

    room_no = int(input('Enter room no to edit: '))

    found = False

    for room in rooms:

        if room['Room no'] == room_no:

            found = True

            print('===Current Room===\n')
            print('Room No: ',room['Room no'])
            print('Room Type: ',room['Room type'])
            print(f'Room Price: ,{room['Room price']}\n')
            
            room['Room type'] = input('Enter room type: ')
            room['Room price'] = int(input('Enter room price: '))
            break

    if found:

        save_room_data()
        print('Room Data updated..')

    else:

        print('Room not found\n')

def save_room_data():

    with open(file_name, 'w', newline='')as file:

        writer = csv.writer(file)

        writer.writerow(['Room no','Room type','Room price'])

        for room in rooms:

            writer.writerow([
                room['Room no'],
                room['Room type'],
                room['Room price']
            ])

def load_room_data():

    rooms.clear()

    try:
        with open(file_name, 'r') as file:

            reader = csv.DictReader(file)

            for row in reader:

                rooms.append({
                    'Room no': int(row['Room no']),
                    'Room type': row['Room type'],
                    'Room price': int(row['Room price'])
                })
    
    except FileNotFoundError:
        pass


while True:
    print('''
1. Add Rooms
2. View Rooms
3. Edit Room Details
4. Exit''')
    
    choice = input('Enter your choice: ')

    if choice =='1':
        add_rooms()

    elif choice =='2':
        view_rooms()

    elif choice =='3':
        edit_rooms()

    elif choice =='4':
        print('\nExiting...')
        
    else:
        print('Choose a valid choice: ')