def handle_user_input(emp_system):
    def add_employee(emp_system):
        pass

    def delete_employee(emp_system):
        pass

    def update_employee_position(emp_system):
        pass

    def update_employee_salary(emp_system):
        pass

    def generate_reports(emp_system):
        pass

    print("\nAvailable operations:")
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Update Employee Position")
    print("4. Update Employee Salary")
    print("5. Generate Reports")
    print("6. Exit")
    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            add_employee(emp_system)
        elif choice == '2':
            delete_employee(emp_system)
        elif choice == '3':
            update_employee_position(emp_system)
        elif choice == '4':
            update_employee_salary(emp_system)
        elif choice == '5':
            generate_reports(emp_system)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
