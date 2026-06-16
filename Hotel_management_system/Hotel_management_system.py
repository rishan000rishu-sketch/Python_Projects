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

def check_out():

    load_room_data()

    room_no = int(input('Enter Room No: '))

    for room in rooms:

        if room['Room no'] == room_no:

            if room['Room status'] != 'Occupied':

                print('Room Not Occupied !')
                return
            
            days = int(input('Enter No Days Stayed: '))

            total = room['Room price'] * days

            save_bill(
                room_no,
                room['Room price'],
                days,
                total
            )

            room['Room status'] = 'Available'
            save_room_data()

            print('\nCheck Out Successful...')
            print('Bill Amount: ',total)
            return
        
    print('Room Not Found !')

def save_bill(room_no, price, days, total):

    bill_id = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    with open(bill_file, 'a', newline='') as file:

        writer = csv.writer(file)

        if os.path.getsize(bill_file) ==0:
            writer.writerow(['Bill_ID','Room NO','Room Price','Days Stay','Total Amount'])

        writer.writerow([
            bill_id,
            room_no,
            price,
            days,
            total
        ])            

while True:

    print("\n===== HOTEL MANAGEMENT SYSTEM =====")
    print("1. Display Rooms")
    print("2. Book Room")
    print("3. Check In")
    print("4. Check Out")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        display_rooms()

    elif choice == "2":
        book_room()

    elif choice == "3":
        check_in()

    elif choice == "4":
        check_out()

    elif choice == "5":
        print("Thank You For Coming 😊")
        break

    else:
        print("Invalid Choice!")
