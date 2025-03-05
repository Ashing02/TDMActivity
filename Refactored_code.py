def get_salary_input():
    while True:
        try:
            salary = float(input("Enter your monthly salary: "))
            if salary < 0:
                raise ValueError("Salary cannot be negative.")
            return salary
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid salary.")

salary = get_salary_input()
calculator = SalaryCalculator(salary)
print(f"Net Salary: {calculator.compute_net_salary():.2f}")
