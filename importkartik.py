import os
FILENAME = "employees.txt"

def load_data():
    employees = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                emp = {
                    "id": data[0],
                    "name": data[1],
                    "tasks": data[2],
                    "score": data[3],
                    "appraisal": data[4]
                }
                employees.append(emp)
    return employees


def save_data(employees):
    with open(FILENAME, "w") as file:
        for emp in employees:
            file.write(f"{emp['id']},{emp['name']},{emp['tasks']},{emp['score']},{emp['appraisal']}\n")

def add_employee(employees):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    tasks = input("Enter Tasks Completed: ")
    score = input("Enter Performance Score (out of 10): ")
    appraisal = input("Enter Appraisal Remark: ")

    employee = {
        "id": emp_id,
        "name": name,
        "tasks": tasks,
        "score": score,
        "appraisal": appraisal
    }

    employees.append(employee)
    save_data(employees)
    print("Employee added successfully!")


def view_employees(employees):
    if not employees:
        print("No employee records found.")
        return

    print("\n--- Employee Performance Details ---")
    for emp in employees:
        print("----------------------------------")
        print("Employee ID :", emp["id"])
        print("Name        :", emp["name"])
        print("Tasks       :", emp["tasks"])
        print("Score       :", emp["score"])
        print("Appraisal   :", emp["appraisal"])


def search_employee(employees):
    emp_id = input("Enter Employee ID to search: ")
    for emp in employees:
        if emp["id"] == emp_id:
            print("\nEmployee Found")
            print("Name      :", emp["name"])
            print("Tasks     :", emp["tasks"])
            print("Score     :", emp["score"])
            print("Appraisal :", emp["appraisal"])
            return
    print("Employee not found!")


def main():
    employees = load_data()

    while True:
        print("\n===== Employee Performance Tracker =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            view_employees(employees)
        elif choice == "3":
            search_employee(employees)
        elif choice == "4":
            print("Exiting system. Thank you!")
            break
        else:
            print("Invalid choice. Try again.")


main()