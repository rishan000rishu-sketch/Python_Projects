class Payroll:

    @staticmethod
    def calculate_tax(gross_salary):
        
        if gross_salary <= 25000:
            return 0
        
        elif gross_salary <= 50000:
            return gross_salary * 0.05
        
        elif gross_salary <= 100000:
            return gross_salary * 0.10
        
        else:
            return gross_salary * 0.20
        
    @staticmethod
    def calculate_salary(employee):

        gross_salary = (
            float(employee['Basic_Salary']) + float(employee['Allowance'])
        )

        tax = Payroll.calculate_tax(gross_salary)

        net_salary = (
            gross_salary - float(employee['Deductions']) - tax
        )

        return net_salary, tax, gross_salary