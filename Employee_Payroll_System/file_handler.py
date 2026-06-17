
import os
import csv

FILE_NAME = 'employees.csv'

HEADERS = [
    'Emp_ID',
    'Name',
    'Department',
    'Destinstion',
    'Basic Salary',
    'Allowance',
    'Deductions'
]

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)

def add_employee(employee):
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=HEADERS)
            writer.writerow(employee.to_dict())

def get_all_employees():

    employees  = []

    with open(FILE_NAME, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            employees.append(row)

    return employees

def update_employees(Emp_ID, updated_data):
    employees = get_all_employees()

    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        
        writer.writeheader()

        for emp in employees:
            if emp['Emp_ID'] == Emp_ID:
                emp.update(updated_data())

            writer.writerow(emp)

def delete_employee(Emp_ID):
    employees = get_all_employees()

    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)

        writer.writeheader()

        for emp in employees:
            if emp['Emp_ID'] != Emp_ID:
                writer.writerow(emp)

def search_employees(Emp_ID):
    employees = get_all_employees()

    for emp in employees:
        if emp['Emp_ID'] == Emp_ID:
            return emp
        
    return None