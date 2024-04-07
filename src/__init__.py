class Employee:
  def __init__(self, emp_id, first_name, last_name, date_of_birth, start_year, position, salary):
      self.emp_id = emp_id
      self.first_name = first_name
      self.last_name = last_name
      self.date_of_birth = date_of_birth
      self.start_year = start_year
      self.position = position
      self.salary = salary

  def __str__(self):
      return (f"ID: {self.emp_id}, "
              f"Name: {self.first_name} {self.last_name}, "
              f"Date of Birth: {self.date_of_birth}, "
              f"Start Year: {self.start_year}, "
              f"Position: {self.position}, "
              f"Salary: {self.salary}")