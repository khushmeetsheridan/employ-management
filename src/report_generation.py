from collections import defaultdict

class EmployeeManagementSystem:
    # Existing code for EmployeeManagementSystem

    def generate_department_list(self):
        departments = set(emp.department for emp in self.employees)
        print("List of Departments:")
        for department in departments:
            print("- ", department)

    def generate_employee_list(self):
        print("List of Employees:")
        for emp in self.employees:
            print(f"- ID: {emp.emp_id}, Name: {emp.first_name} {emp.last_name}, Department: {emp.department}")

    def generate_department_avg_age_salary(self):
        department_ages = defaultdict(list)
        department_salaries = defaultdict(list)

        # Calculate average age and salary for each department
        for emp in self.employees:
            department_ages[emp.department].append(emp.calculate_age())
            department_salaries[emp.department].append(emp.salary)

        print("Average Age and Salary for Each Department:")
        for department, ages in department_ages.items():
            avg_age = sum(ages) / len(ages)
            avg_salary = sum(department_salaries[department]) / len(department_salaries[department])
            print(f"- Department: {department}, Average Age: {avg_age:.2f}, Average Salary: ${avg_salary:.2f}")

    def generate_department_employee_details(self):
        department_employees = defaultdict(list)

        # Group employees by department
        for emp in self.employees:
            department_employees[emp.department].append(emp)

        print("Employees in Each Department:")
        for department, employees in department_employees.items():
            print(f"\nDepartment: {department}")
            for emp in employees:
                print(f"- ID: {emp.emp_id}, Name: {emp.first_name} {emp.last_name}, Date of Birth: {emp.date_of_birth}, Salary: ${emp.salary}")
            total_salary = sum(emp.salary for emp in employees)
            print(f"Total Salary for {department}: ${total_salary}")
