contacts = {}

def add_contact():

    name = input('Enter contact name: ')
    phone = int(input('Enter phone number: '))

    contacts[name] = phone

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