from Rooms import rooms, load_room_data, save_room_data

def display_rooms():
    load_room_data()

    print('\n======Available Rooms======\n')

    for room in rooms:

        print(
            f'Room {room['Room no']}',
            f'{room['Room type']}',
            f'₹{room['Room price']}',
            f'{room['Room status']}',
        )

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

    # elif choice == "2":
    #     book_room()

    # elif choice == "3":
    #     check_in()

    # elif choice == "4":
    #     check_out()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
