def is_even_odd(num):

    if num %2 ==0:
        return 'Even'
    else:
        return 'Odd'
    
def main():
        
    try:

        number = int(input('Enter a number'))

        result = is_even_odd(number)

        print(f'The given number {number} is {result}...')

    except ValueError:

        print('Enter a valid number')

main()
              
