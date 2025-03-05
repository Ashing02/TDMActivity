def compute_deductions(gross_salary):
    sss_deduction = 1200
    philhealth_deduction = (gross_salary * 0.05) / 2
    pagibig_deduction = 100
    tax_deduction = 1875  

    total_deductions = sss_deduction + philhealth_deduction + pagibig_deduction + tax_deduction
    net_salary = gross_salary - total_deductions

    return {
        "gross_salary": gross_salary,
        "sss": sss_deduction,
        "philhealth": philhealth_deduction,
        "pagibig": pagibig_deduction,
        "tax": tax_deduction,
        "total_deductions": total_deductions,
        "net_salary": net_salary
    }