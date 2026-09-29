def calculate_salary(basic_salary):
    hra = basic_salary * 0.20
    da = basic_salary * 0.10
    pf = basic_salary * 0.12

    gross_salary = basic_salary + hra + da
    net_salary = gross_salary - pf

    return hra, da, pf, gross_salary, net_salary


def main():
    print("========== EMPLOYEE PAYROLL SYSTEM ==========")

    employees = []

    n = int(input("\nEnter number of employees: "))

    for i in range(n):
        print(f"\nEmployee {i + 1}")

        name = input("Enter employee name: ")
        employee_id = input("Enter employee ID: ")

        while True:
            try:
                basic_salary = float(input("Enter basic salary: ₹"))

                if basic_salary <= 0:
                    print("Salary must be greater than 0.")
                else:
                    break

            except ValueError:
                print("Enter a valid salary.")

        hra, da, pf, gross, net = calculate_salary(basic_salary)

        employees.append({
            "name": name,
            "id": employee_id,
            "basic": basic_salary,
            "hra": hra,
            "da": da,
            "pf": pf,
            "gross": gross,
            "net": net
        })

    print("\n========== PAYROLL DETAILS ==========")

    for employee in employees:
        print(f"\nEmployee Name: {employee['name']}")
        print(f"Employee ID: {employee['id']}")
        print(f"Basic Salary: ₹{employee['basic']:.2f}")
        print(f"HRA: ₹{employee['hra']:.2f}")
        print(f"DA: ₹{employee['da']:.2f}")
        print(f"PF Deduction: ₹{employee['pf']:.2f}")
        print(f"Gross Salary: ₹{employee['gross']:.2f}")
        print(f"Net Salary: ₹{employee['net']:.2f}")


if __name__ == "__main__":
    main()