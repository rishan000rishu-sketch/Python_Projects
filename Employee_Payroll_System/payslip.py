import os
from payroll import Payroll

def generate_slip(employee):

    tax, gross_salary, net_salary = Payroll.calculate_salary(employee)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    PAYSLIP_DIR = os.path.join(BASE_DIR, 'payslips')

    if not os.path.exists(PAYSLIP_DIR):
        os.mkdir(PAYSLIP_DIR)

    file_name = os.path.join(PAYSLIP_DIR, f'payslip_{employee['Emp_ID']}.txt')

    with open(file_name, 'w') as file:

        file.write('==========================\n')
        file.write('     EMPLOYEE PAYSLIP\n')
        file.write('==========================\n')

        file.write(f'Employee_ID   :  {employee['Emp_ID']}\n')
        file.write(f'Name          :  {employee['Name']}\n')
        file.write(f'Department    :  {employee['Department']}\n')
        file.write(f'Designation   :  {employee['Designation']}\n\n')

        file.write(f'Basic_Salary  :  {employee['Basic_Salary']}\n')
        file.write(f'Allowance     :  {employee['Allowance']}\n')
        file.write(f'Deductions    :  {employee['Deductions']}\n\n')

        file.write(f'Gross_Salary  :  {gross_salary:.2f}\n')
        file.write(f'Tax           :  {tax:.2f}\n')
        file.write(f'Net_Salary    :  {net_salary:.2f}\n')

        file.write('==========================\n')

    return file_name