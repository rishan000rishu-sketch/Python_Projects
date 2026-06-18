from employee import Employee
from file_handler import *

create_file()

def add_new_employee():

    emp_id = input('Employee_ID: ')
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

    add_employee(employee)
    print('\nEmployee Added Successfully')


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

    except Exception as e:
        print(f"Error: {e}")
        