def compute_sss():
    return 1200

def compute_philhealth(gross_salary):
    return (gross_salary * 0.05) / 2

def compute_pagibig():
    return 100

def compute_tax():
    return 1875

def compute_total_deductions(gross_salary):
    sss = compute_sss()
    philhealth = compute_philhealth(gross_salary)
    pagibig = compute_pagibig()
    tax = compute_tax()

    return sss + philhealth + pagibig + tax

def compute_net_salary(gross_salary):
    total_deductions = compute_total_deductions(gross_salary)
    return gross_salary - total_deductions

def compute_deductions(gross_salary):
    sss = compute_sss()
    philhealth = compute_philhealth(gross_salary)
    pagibig = compute_pagibig()
    tax = compute_tax()
    total_deductions = sss + philhealth + pagibig + tax
    net_salary = gross_salary - total_deductions

    return {
        "gross_salary": gross_salary,
        "sss": sss,
        "philhealth": philhealth,
        "pagibig": pagibig,
        "tax": tax,
        "total_deductions": total_deductions,
        "net_salary": net_salary
    }


# Example usage
gross_salary = 50000
salary_details = compute_deductions(gross_salary)

for key, value in salary_details.items():
    print(f"{key}: {value:.2f}")
