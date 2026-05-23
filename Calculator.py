import math

def sub(num1,num2):
    return num1-num2

def add(num1,num2):
    return num1+num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

def sqrt(num):
    return math.sqrt(num)

def pow(num1,num2):
    return math.pow(num1,num2)

def sin(num):
    return math.sin(num)

def cos(num):
    return math.cos(num)

def tan(num):
    return math.tan(num)

def log(num):
    return math.log(num)

while True:
    print('1.  Addition')
    print('2.  Subtraction')
    print('3.  Multiplication')
    print('4.  Division')
    print('5.  Sqrt')
    print('6.  Power')
    print('7.  Sin')
    print('8.  Cos')
    print('9.  Tan')
    print('10. Log')
    print('11. Exit')

    option=input('Select your option: ')

    if option in('1','2','3','4','6'):
        num1=float(input('Enter first number: '))
        num2=float(input('Enter second number: '))

        if option=='1':   
            print('result is: ',add(num1,num2))

        elif option=='2':
            print('result is: ',sub(num1,num2))

        elif option=='3':
            print('result is: ',mul(num1,num2))

        elif option=='4':
            print('result is: ',div(num1,num2))

        elif option=='6':
            print(f'The Power of the {num1} is: ',pow(num1,num2))

    elif option in('5','7','8','9','10'):
        num=float(input('Enter a number: '))

        if option=='5':
            print(f'Sqrt of {num} is: ',sqrt(num))

        elif option=='7':
            print(f'Sin of {num} is: ',sin(num))

        elif option=='8':
            print(f'Cos of {num} is: ',cos(num))

        elif option=='9':
            print(f'Tan of {num} is: ',tan(num))

        elif option=='10':
            print(f'Log of {num} is: ',log(num))

    elif option=='11':
        print('Exiting program....')
        break

    else:
        print('invalid option')
