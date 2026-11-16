from student import *

while True:
    print("\n1. Add Student")
    print("2. Show All Students")
    print("3. Update Student")
    print("4. Remove Student")
    print("5. Search Student")
    print("6. Exit")
    
    choice = input("enter your choice: ").strip()
    
    if choice == "1":
        addStudent()
    elif choice == "2":
        showAllStudents()
    elif choice == "3":
        updateStudent()
    elif choice == "4":
        removeStudent()
    elif choice == "5":
        searchStudent()
    elif choice == "6":
        break
    else:
        print("invalid choice!")