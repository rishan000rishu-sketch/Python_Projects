from employee import Employee
from file_handler import *

from payroll import Payroll
from payslip import generate_slip

create_file()

def add_new_employee():

    emp_id = input('Employee_ID: ')

    employees = get_all_employees()

    for emp in employees:

        if emp['Emp_ID']==emp_id:
            print('\nEmployee ID Already Existed !')
            return
        
    name = input('Name: ')
    department = input('Department: ')
    designation = input('Designation: ')

    basic_salary = float(input('Basic Salary: '))
    allowance = float(input('Allowance: '))
    deductions = float(input('Deductions: '))

    employee = Employee(
        emp_id,
        name,
        department,
        designation,
        basic_salary,
        allowance,
        deductions
    )

    add_employees(employee)
    print('\nEmployee Added Successfully')

def view_employees():

    employees = get_all_employees()

    if not employees:
        print('\nEmployees Not Found !\n')
        return
    
    for emp in employees:
        print('-'*40)

        for key, value in emp.items():
            print(f'{key}: {value}')

def search_employee():
    
    emp_id = input('Employee_ID: ')

    employee = search_employees(emp_id)

    if employee:
        print(employee)
    else:
        print('\nEmployee Not Found')

def update_employee():

    emp_id = input('Employee_ID: ')

    employees= get_all_employees()

    if not employees:
        print('Employee Is Not Found !')
        return
    
    new_department = input('Enter New Department: ')

    update_employees(emp_id,{"Department": new_department})

    print('Employee Updated.')

def delete_employee():

    emp_id = input('Employee_ID: ')

    delete_employees(emp_id)

    print|('Employee Deleted.')

def calculate_salary():

    emp_id = input('Employee_ID: ')

    employee =  search_employees(emp_id)

    if employee:

        gross, tax, net= Payroll.calculate_salary(employee)

        print(f'\nSalary Details Of {employee['Name']}')
        print('-' *30,'\n')
        print(f'Gross_Salary : {gross:.2f}')
        print(f'Tax          : {tax:.2f}')
        print(f'Net_Salary   : {net:.2f}')

    else:
        print('Employee Not Found !')

def create_payslip():

    emp_id = input('Employee_ID: ')

    employee = search_employees(emp_id)

    if employee:

        filename = generate_slip(employee)

        print(f'Payslip Generated: {filename}')
    
    else:
        print('Employee Not Found !')
        

while True:

    print("\n===== EMPLOYEE PAYROLL SYSTEM =====")

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Calculate Salary")
    print("7. Generate Payslip")
    print("8. Exit")

    choice = input("\nEnter Choice: ")

    try:

        if choice == "1":
            add_new_employee()

        elif choice == '2':
            view_employees()

        elif choice == '3':
            search_employee()

        elif choice == '4':
            update_employee()

        elif choice =='5':
            delete_employee()

        elif choice == '6':
            calculate_salary()

        elif choice == '7':
            create_payslip()

        elif choice == '8':
            print('\nGood By 😊')

        else:
            print('Invalid Option !')

    except Exception as e:
        print(f"Error: {e}")
