def _main_menu():
  employees = {
      101 : {"name" :"Ayush" , "age" : 20 , "department" : "Intern" , "salary" : 10000},
      102 : {"name" :"Tushar" , "age" : 24 , "department" : "Finance" , "salary" : 40000},
      103 : {"name" :"Suraj" , "age" : 27 , "department" : "Marketing" , "salary" : 80000},
      104 : {"name" :"Adhyaraj" , "age" : 30 , "department" : "HR" , "salary" : 100000}
  }
  while(True):
    print("Employee Management System ")
    print("\n 1. Add Employee")
    print("\n 2. View Employee")
    print("\n 3. Search For Employee")
    print("\n 4. Exit")
    choice = input("Enter your choice : ")
    if choice == 1:
      add_employee(employees)
    if choice == 2:
      view_employee(employees)
    if choice == 3:
      search_employee(employees)
    if choice == 4:
      print("Thank you for visiting")
      break
    else:
      print("Invalid input ")

def add_employee(employees):
  try:
    emp_id = input("Enter employee Id: ")
    if emp_id in employees:
      print("Employee Already present")
      return
    else:
      name = input("Enter employee name: ")
      age = int(input("Enter emp age: "))
      department = input("Enter emp department")
      salary = int(input("Enter emp salary"))
      employees[emp_id] = {"name" : name , "age" : age , "department" : department , "salary" : salary}
      print("EMployee added successfully")
  except ValueError:
        print("Invalid input")
def view_employee(employees):
  if  not employees:
    print("No employee available")
    return
  print("\nID    Name      Age   Department  Salary")
  for i , j in employees.items():
    print(f"{i :<5} {j["name"]:<10} {j["age"]:<5} {j["department"]:<15 } {j["salary"]:<10 }")
def search_employee(employees):
  try:
    emp_id = input("emter employee id: ")
    if emp_id in employees:
      details = employees[emp_id]
      print(f"ID: {emp_id} \nName : {details["name"]} \nAge : {details['age'] } \nDepartment : {details['department']} \nSalary : {details['salary'] }")
    else:
      print("employee not found")
  except ValueError:
    print("Invalid input")
if __name__ == "__main__":
  _main_menu() 