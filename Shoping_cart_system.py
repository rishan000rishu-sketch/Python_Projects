cart = []

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
        item_name = input('Enter item name to add: ')
        item_price = float(input('Enter item price to add: '))

        item = {
            'name':item_name,
            'price':item_price
        }

        cart.append(item)
        print(f'{item_name} added to cart successfully...')

    elif choice =='2':
        if len(cart) ==0:
            print('Cart is empty!!!')
        else:
            print('\n=====Cart Items=====')
            for item in cart:
                print(f'{item['name']} - ₹{item['price']}')

    elif choice =='3':
        item_name = input('Enter item name to remove: ')

        found = False
        for item in cart:
            if item['name'].lower() == item_name.lower():
                cart.remove(item)
                print(f'{item_name} removed successfully...')
                
                found = True
                break
        if not found:
            print('Item not in cart!!')

    elif choice =='4':
        total = 0

        for item in cart:
            total += item['price']

        print(f'Total Bill: ₹{total}')

    elif choice =='5':
        print('\nThank you for shopping 😊')
        break

    else:
        print('Invalid choice!!!!')