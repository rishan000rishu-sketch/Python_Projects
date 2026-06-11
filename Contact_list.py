contacts = {}

file_name = 'contact.txt'

def add_contact():

    name = input('Enter contact name: ')
    phone = int(input('Enter phone number: '))

    contacts[name] = phone

    with open(file_name, 'r') as file:

        for line in file:

            if f'Name: {name},Phone: {phone}'== line.strip():

                print('\nContact already exists !')
                return

    with open(file_name, 'a') as file:

            file.write(f'Name: {name},Phone: {phone}\n')
    
    print('Contact added successfully')

def view_contacts():

    if len(contacts) ==0:
        print('No contacts found!')
    else:
        
        print('===Contact List===')

        for name, phone in contacts.items():
            
            print('\nName: ',name)
            print('Phone: ',phone)
            print('-' *20)

def search_contact():

    name = input('Enter contact name: ')
    
    if name in contacts:
        phone = contacts[name]

        print('\nName: ',name)
        print('Phone: ',phone)

    else:
        print('Contact not found!')

def delete_contact():

    name = input('Enter contact name: ')

    if name in contacts:

        del contacts[name]
        print('Contact deleted successfully...')

    else:

        print('Contact not found!')

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