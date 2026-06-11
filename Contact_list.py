import os

contacts = {}

file_name = 'contact.txt'

def add_contact():

    load_data()

    name = input('Enter contact name: ')
    phone = int(input('Enter phone number: '))

    if name in contacts:
        print('Contact already Exists !')

    else:
        contacts[name] = phone
        save_data()

        print('Contact Added successfully...')

def view_contacts():

    load_data()

    if len(contacts) ==0:
        print('No contacts found!')
    else:
        
        print('===Contact List===')

        for name, phone in contacts.items():
            
            print('\nName: ',name)
            print('Phone: ',phone)
            print('-' *20)

def search_contact():

    load_data()
    name = input('Enter contact name: ')
    
    if name in contacts:

        print('\nName: ',name)
        print('Phone: ',contacts[name])

    else:
        print('Contact not found!')

def delete_contact():
    
    load_data()
    name = input('Enter contact name: ')

    if name in contacts:

        del contacts[name]
        save_data()

        print('Contact deleted..')
    else:
        print('Contact not found !')

def load_data():

    if not os.path.exists(file_name):
        return
    
    try:
        
        with open(file_name, 'r')as file:

            for line in file:

                parts = line.strip().split(',')

                name = parts[0].split(':')[1].strip()

                phone = parts[1].split(':')[1].strip()

                contacts[name] = phone

    except FileNotFoundError:
        pass

def save_data():

    with open(file_name,'w')as file:

        for name,phone in contacts.items():

            file.write(f'Name: {name},Phone: {phone}\n')

while True:

    print('''
=======CONTACT BOOK=======\n
1. Add Contact
2. View all contacts
3. Search Contact
4. Delete Contact
5. Exit''')
        
    option = input('Enter your option: ')

    if option =='1':
        add_contact()
 
    elif option =='2':
        view_contacts()

    elif option =='3':
        search_contact()

    elif option =='4':
        delete_contact()

    elif option =='5':
        break
    
    else:
        print('Please choose a valid option!!')