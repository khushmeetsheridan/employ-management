class EmployeeManagementSystem:
  def __init__(self):
      self.employees = []

  def add_employee(self, employee):
      self.employees.append(employee)
      print(f"Added employee: {employee}")

  def delete_employee(self, employee_id):
      for i, emp in enumerate(self.employees):
          if emp.emp_id == employee_id:
              deleted_employee = self.employees.pop(i)
              print(f"Deleted employee: {deleted_employee}")
              return
      print(f"Employee with ID {employee_id} not found.")

  def update_employee_position(self, employee_id, new_position):
      for emp in self.employees:
          if emp.emp_id == employee_id:
              old_position = emp.position
              emp.position = new_position
              print(f"Updated employee {emp.first_name} {emp.last_name}'s position from {old_position} to {new_position}")
              return
      print(f"Employee with ID {employee_id} not found.")

  def update_employee_salary(self, employee_id, new_salary):
      for emp in self.employees:
          if emp.emp_id == employee_id:
              old_salary = emp.salary
              emp.salary = new_salary
              print(f"Updated employee {emp.first_name} {emp.last_name}'s salary from {old_salary} to {new_salary}")
              return
      print(f"Employee with ID {employee_id} not found.")

  def generate_reports(self):
      for emp in self.employees:
          print(emp)
