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