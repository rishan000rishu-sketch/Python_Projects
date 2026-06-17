
class Employee:

    def __init__(
        self,
        emp_id,
        name,
        department,
        destination,
        basic_salary,
        allowance,
        deductions
    ):
        
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.destination = destination
        self.basic_salary = basic_salary
        self.allowance = allowance
        self.deductions = deductions

    def to_dict(self):

        return{
            'Emp_ID': self.emp_id,
            'Name': self.name,
            'Department': self.department,
            'Destination': self.destination,
            'Basic_Salary': self.basic_salary,
            'Allowance': self.allowance,
            'Deductions': self.deductions
        }
    