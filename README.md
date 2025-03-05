# Final Report
## Team Members & Contributions:
- Jireh Xaris Dumindin - Project Manager
- Rozel Galceran - Lead Developer 
- Wendelyn Paller - Refactoring Specialist
- Ashley Rose Daug-  Lead Developer
-Rhendyll Mae Almerol-  Tester/Dcumenter
-Kim Ryan Orencia -  Lead Developer

## Technical Debt Identified:
- Poor variable naming
- Lack of modularity
- Hardcoded values
- No error handling
- Code duplication

## Refactoring Improvements:
- Used descriptive variable names
- Separated logic into functions
- Implemented OOP structure
- Added input validation and error handling
- Optimized printing logic

## Challenges & Solutions:
- **Merge Conflicts:** Resolved by reviewing PRs before merging.
- **Edge Cases:** Handled invalid salary inputs properly.
- **Testing Issues:** Verified with different salary inputs.

 REFRACTORED CHANGES:

 # ===========================
# Role: Tester & Documenter
# Function: Get user salary input with validation
# ===========================

def get_salary_input():
    """Prompts the user to enter a valid salary amount."""
    while True:
        try:
            salary = float(input("Enter your monthly salary: "))
            if salary <= 0:
                print("Salary must be a positive number. Please try again.")
            else:
                return salary
        except ValueError:
            print("Invalid input! Please enter a valid numeric value for salary.")

# ===========================
# Role: Lead Developer
# Function: Modular deduction calculations
# ===========================

def calculate_sss_deduction():
    """Returns the fixed SSS deduction."""
    return 1200

def calculate_philhealth_deduction(salary, philhealth_rate=0.05):
    """Calculates PhilHealth deduction based on a percentage of salary."""
    return (salary * philhealth_rate) / 2

def calculate_pagibig_deduction():
    """Returns the fixed Pag-IBIG deduction."""
    return 100

def calculate_tax_deduction():
    """Returns a fixed tax deduction (assumption for simplicity)."""
    return 1875

def calculate_total_deductions(sss, philhealth, pagibig, tax):
    """Calculates the total amount of deductions."""
    return sss + philhealth + pagibig + tax

def calculate_net_salary(salary, total_deductions):
    """Computes the net salary after deductions."""
    return salary - total_deductions

# ===========================
# Role: Refactoring Specialist
# Function: Improved output format & reduced redundancy
# ===========================

def display_results(salary, sss, philhealth, pagibig, tax, total_deductions, net_salary):
    """Displays the detailed breakdown of deductions and net salary."""
    deductions = {
        "Gross Salary": salary,
        "SSS Deduction": sss,
        "PhilHealth Deduction": philhealth,
        "Pag-IBIG Deduction": pagibig,
        "Tax Deduction": tax,
        "Total Deductions": total_deductions,
        "Net Salary": net_salary
    }

    print("\n=== Salary Deduction Breakdown ===")
    for label, value in deductions.items():
        print(f"{label}: {value:.2f}")

# ===========================
# Role: Git Manager
# Function: Finalized program execution with Git version control
# ===========================

def main():
    """Main function to run the Salary Deduction Calculator."""
    salary = get_salary_input()
    sss = calculate_sss_deduction()
    philhealth = calculate_philhealth_deduction(salary)
    pagibig = calculate_pagibig_deduction()
    tax = calculate_tax_deduction()
    total_deductions = calculate_total_deductions(sss, philhealth, pagibig, tax)
    net_salary = calculate_net_salary(salary, total_deductions)

    display_results(salary, sss, philhealth, pagibig, tax, total_deductions, net_salary)

if __name__ == "__main__":
    main()



