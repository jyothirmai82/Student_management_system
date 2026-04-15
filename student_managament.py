import os
FILE_NAME = "students.txt"

def add_student():
    id = input("Enter ID: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{id},{name},{marks}\n")

    print("Student added successfully!\n")

def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return
    with open(FILE_NAME, "r") as f:
        data = f.readlines()
    if not data:
        print("No students available.\n")
        return
    print("\n--- Student List ---")
    for line in data:
        id, name, marks = line.strip().split(",")
        print(f"ID: {id}, Name: {name}, Marks: {marks}")
    print()

def search_student():
    search_id = input("Enter ID to search: ")
    with open(FILE_NAME, "r") as f:
        for line in f:
            id, name, marks = line.strip().split(",")
            if id == search_id:
                print(f"Found: ID={id}, Name={name}, Marks={marks}\n")
                return
    print("Student not found.\n")

def delete_student():
    delete_id = input("Enter ID to delete: ")
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()
    with open(FILE_NAME, "w") as f:
        found = False
        for line in lines:
            id, name, marks = line.strip().split(",")
            if id != delete_id:
                f.write(line)
            else:
                found = True
    if found:
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")

def menu():
    while True:
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
menu()