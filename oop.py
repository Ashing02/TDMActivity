class SalaryCalculator:
    def __init__(self, salary):
        self.salary = salary
        self.sss = 1200
        self.pagibig = 100
        self.tax = 1875
        self.philhealth = (salary * 0.05) / 2

    def compute_deductions(self):
        return self.sss + self.pagibig + self.tax + self.philhealth

    def compute_net_salary(self):
        return self.salary - self.compute_deductions()

salary = float(input("Enter your monthly salary: "))
calculator = SalaryCalculator(salary)
print(f"Net Salary: {calculator.compute_net_salary():.2f}")