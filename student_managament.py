import os

FILE_NAME = "students.txt"

def ensure_file():
    if not os.path.exists(FILE_NAME):
        open(FILE_NAME, "w").close()

def add_student():
    id = input("Enter ID: ").strip()
    name = input("Enter Name: ").strip()
    marks = input("Enter Marks: ").strip()
    if not id or not name or not marks:
        print("All fields are required!\n")
        return
    with open(FILE_NAME, "a") as f:
        f.write(f"{id},{name},{marks}\n")
    print("Student added successfully!\n")

def view_students():
    ensure_file()
    with open(FILE_NAME, "r") as f:
        data = f.readlines()
    if not data:
        print("No students found.\n")
        return
    print("\n--- Student List ---")
    for line in data:
        id, name, marks = line.strip().split(",")
        print(f"ID: {id}, Name: {name}, Marks: {marks}")
    print()

def search_student():
    search_id = input("Enter ID to search: ").strip()
    found = False
    with open(FILE_NAME, "r") as f:
        for line in f:
            id, name, marks = line.strip().split(",")
            if id == search_id:
                print(f"Found: ID={id}, Name={name}, Marks={marks}\n")
                found = True
                break
    if not found:
        print("Student not found.\n")

def delete_student():
    delete_id = input("Enter ID to delete: ").strip()
    found = False
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()
    with open(FILE_NAME, "w") as f:
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

def update_student():
    update_id = input("Enter ID to update: ").strip()
    found = False
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()
    with open(FILE_NAME, "w") as f:
        for line in lines:
            id, name, marks = line.strip().split(",")
            if id == update_id:
                new_name = input("Enter new name: ").strip()
                new_marks = input("Enter new marks: ").strip()
                f.write(f"{id},{new_name},{new_marks}\n")
                found = True
            else:
                f.write(line)
    if found:
        print("Student updated successfully!\n")
    else:
        print("Student not found.\n")

def menu():
    ensure_file()
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.\n")

menu()