# Configuration rules for salary calculation
SALARY_RULES = {
    "hra_percentage": 20.0,       
    "da_percentage": 10.0,       
    "tax_percentage": 15.0,       
    "provident_fund": 1800.0     
}

def get_valid_float(prompt: str) -> float:
    """Validates and returns a numeric float input from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: Value cannot be negative. Please try again.")
                continue
            return value
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

def calculate_gross_salary(basic_salary: float, rules: dict) -> dict:
    """Calculates components of gross salary based on configuration rules."""
    hra = basic_salary * (rules["hra_percentage"] / 100)
    da = basic_salary * (rules["da_percentage"] / 100)
    gross_salary = basic_salary + hra + da
    return {
        "basic": basic_salary,
        "hra": hra,
        "da": da,
        "gross": gross_salary
    }

def calculate_deductions(gross_salary: float, rules: dict) -> dict:
    """Calculates total deductions based on configuration rules."""
    tax = gross_salary * (rules["tax_percentage"] / 100)
    pf = rules["provident_fund"]
    total_deductions = tax + pf
    return {
        "tax": tax,
        "pf": pf,
        "total_deductions": total_deductions
    }

def generate_salary_breakdown(employee_name: str, basic_salary: float, rules: dict):
    """Computes full salary details and prints a structured breakdown."""
    
    earnings = calculate_gross_salary(basic_salary, rules)
   
    deductions = calculate_deductions(earnings["gross"], rules)
    
   
    net_salary = earnings["gross"] - deductions["total_deductions"]

   
    print("\n" + "=" * 40)
    print(f" SALARY BREAKDOWN FOR: {employee_name.upper()} ")
    print("=" * 40)
    print(f" Basic Salary        : ₹{earnings['basic']:,.2f}")
    print(f" HRA ({rules['hra_percentage']}%): ₹{earnings['hra']:,.2f}")
    print(f" DA ({rules['da_percentage']}%): ₹{earnings['da']:,.2f}")
    print("-" * 40)
    print(f" Gross Salary        : ₹{earnings['gross']:,.2f}")
    print("-" * 40)
    print(f" Tax ({rules['tax_percentage']}%): ₹{deductions['tax']:,.2f}")
    print(f" Provident Fund (PF) : ₹{deductions['pf']:,.2f}")
    print(f" Total Deductions    : ₹{deductions['total_deductions']:,.2f}")
    print("=" * 40)
    print(f" NET SALARY          : ₹{net_salary:,.2f}")
    print("=" * 40)

def main():
    print("--- Employee Salary Calculator ---")
    
 
    emp_name = input("Enter Employee Name: ").strip()
    if not emp_name:
        emp_name = "Anonymous Employee"
        
    basic_salary = get_valid_float("Enter Basic Salary: ₹")
    
    
    generate_salary_breakdown(emp_name, basic_salary, SALARY_RULES)

if __name__ == "__main__":
    main()
