students = []

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students.append({"name": name, "marks": marks})
    print("Student added!\n")

def view_students():
    if not students:
        print("No students found!\n")
        return
    for i, s in enumerate(students):
        print(i+1, s["name"], "-", s["marks"])
    print()

def search_student():
    name = input("Enter name to search: ")
    for s in students:
        if s["name"].lower() == name.lower():
            print("Found:", s["name"], "-", s["marks"])
            return
    print("Student not found!\n")

def delete_student():
    name = input("Enter name to delete: ")
    for s in students:
        if s["name"].lower() == name.lower():
            students.remove(s)
            print("Deleted!\n")
            return
    print("Not found!\n")

while True:
    print("==== Student Management System ====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice!\n")