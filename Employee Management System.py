employees = []

def add_employee():
    name = input("Enter employee name: ")
    age = input("Enter employee age: ")
    department = input("Enter employee department: ")
    employees.append({"name": name, "age": age, "department": department})
    print("Employee added successfully!")

def view_employees():
    if not employees:
        print("No employees found!")
    else:
        for i, emp in enumerate(employees, 1):
            print(f"{i}. Name: {emp['name']}, Age: {emp['age']}, Department: {emp['department']}")

def delete_employee():
    view_employees()
    if employees:
        emp_index = int(input("Enter the employee number to delete: ")) - 1
        if 0 <= emp_index < len(employees):
            employees.pop(emp_index)
            print("Employee deleted successfully!")
        else:
            print("Invalid employee number!")

while True:
    print("\n1. Add Employee\n2. View Employees\n3. Delete Employee\n4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
