def get_philhealth_deduction(salary):
    return (salary * 0.05) / 2

def compute_deductions(salary):
    sss = 1200
    pagibig = 100
    tax = 1875
    philhealth = get_philhealth_deduction(salary)
    
    total_deductions = sss + pagibig + tax + philhealth
    return total_deductions, salary - total_deductions