from Rooms import rooms, load_room_data, save_room_data
from datetime import datetime
import os
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

customer_file = os.path.join(BASE_DIR, "customers.csv")
bill_file = os.path.join(BASE_DIR, "bills.csv")

def display_rooms():
    load_room_data()

    if len(rooms) ==0:
        print('\nRooms not Found !')
        return

    print('\n======Available Rooms======\n')

    for room in rooms:

        print(f'''
Room No     : {room['Room no']}
Room Type   : {room['Room type']}
Room Price  : {room['Room price']}
Room Status : {room['Room status']}
''')

def book_room():

    room_no = int(input('Enter Room No: '))

    for room in rooms:

        if room['Room no'] == room_no:

            if room['Room status'] != 'Available':
                print('\nRoom Not Available !')
                return

            name = input('Enter Customer Name: ')
            phone = int(input('Enter Phone No: '))
            days = int(input('Days Stay: '))

            with open(customer_file, 'a', newline='') as file:

                writer = csv.writer(file)

                if os.path.getsize(customer_file) ==0:
                    writer.writerow(['Room no','Customer Name','Phone','Days Stay'])

                writer.writerow([room_no,name,phone,days])

                room['Room status'] = 'Booked'

                save_room_data()
                print('Room Booked Successfully..')
                return
            
    print('Room Not Found !')

def check_in():

    load_room_data()

    room_no = int(input('Enter Room No: '))

    for room in rooms:

        if room['Room no'] == room_no:

            if room['Room status'] == 'Booked':
                
                room['Room status'] = 'Occupied'

                save_room_data()
                print('Room Check In Successful..')
                return
            
            print('Room Not Booked !')
            return

    print('Room Not Found !')


while True:

    print("\n===== HOTEL MANAGEMENT SYSTEM =====")
    print("1. Display Rooms")
    print("2. Book Room")
    print("3. Check In")
    print("4. Check Out")
    print("5. Save bill")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        display_rooms()

    elif choice == "2":
        book_room()

    elif choice == "3":
        check_in()

    # elif choice == "4":
    #     check_out()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
