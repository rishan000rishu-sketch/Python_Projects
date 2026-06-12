import os

cart = {}

file_name = 'Cart.txt'

def save_data():

    with open(file_name, 'w')as file:

        for name, price in cart.items():

            file.write(f'Name: {name},Price: {price}\n')

def load_data():

    if not os.path.exists(file_name):
        return
    
    try:
        with open(file_name, 'r')as file:

            for line in file:

                parts = line.strip().split(',')

                name = parts[0].split(':')[1].strip()
                price = parts[1].split(':')[1].strip()

                cart[name] = int(price)

    except FileNotFoundError:
        pass


while True:
    print('''
1. Add Items
2. View Cart
3. Remove Items
4. Calculate Total bill
5. Exit 
''')
    
    choice = input('Enter tour choice: ')

    if choice =='1':
        load_data()
        name = input('Enter item name to add: ')
        price = int(input('Enter item price to add: '))

        cart[name] = price

        save_data()
        print(f'{name} added to cart...')

    elif choice =='2':
        load_data()
        if len(cart) ==0:
            print('Cart is empty!!!')
        else:
            print('\n=====Cart Items=====\n')
            for name, price in cart.items():
                print(f'{name} - ₹{price}')
                

    elif choice =='3':

        load_data()
        name = input('Enter item name to remove: ')

        if name in cart:
    
            del cart[name]
            save_data()

            print(f'{name} removed successfully...')
        
        else:
            print('Item not in the cart !')

    elif choice =='4':

        load_data()
        total = 0

        for name in cart:
            total += cart[name]

        print(f'Total Bill: ₹{total}')

    elif choice =='5':
        print('\nThank you for shopping 😊')
        break

    else:
        print('Invalid choice!!!!')