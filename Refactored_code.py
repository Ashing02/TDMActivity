class SalaryCalculator:
    def __init__(self, gross_salary):
        self.gross_salary = gross_salary

    def compute_sss(self):
        return 1200

    def compute_philhealth(self):
        return (self.gross_salary * 0.05) / 2

    def compute_pagibig(self):
        return 100

    def compute_tax(self):
        return 1875

    def compute_total_deductions(self):
        return (
            self.compute_sss() +
            self.compute_philhealth() +
            self.compute_pagibig() +
            self.compute_tax()
        )

    def compute_net_salary(self):
        return self.gross_salary - self.compute_total_deductions()

    def compute_deductions(self):
        sss = self.compute_sss()
        philhealth = self.compute_philhealth()
        pagibig = self.compute_pagibig()
        tax = self.compute_tax()
        total_deductions = sss + philhealth + pagibig + tax
        net_salary = self.gross_salary - total_deductions

        return {
            "gross_salary": self.gross_salary,
            "sss": sss,
            "philhealth": philhealth,
            "pagibig": pagibig,
            "tax": tax,
            "total_deductions": total_deductions,
            "net_salary": net_salary
        }

# Example usage
gross_salary = 50000
calculator = SalaryCalculator(gross_salary)
salary_details = calculator.compute_deductions()

for key, value in salary_details.items():
    print(f"{key}: {value:.2f}")
