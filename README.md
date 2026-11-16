# 🎓 Student Management System

> A robust command-line Student Management System built with Python, featuring persistent JSON storage and structured incremental Git workflow.

---

## 🚀 Features

- *Add Students*: Register new student profiles with ID, name, surname, age, and grades.
- *View Records*: Display all registered students in a clean, formatted layout.
- *Search & Filter*: Quickly find specific student details.
- *Remove Records*: Securely delete student profiles by ID.
- *Data Persistence*: Automatic data loading and saving via local JSON storage (students.json).

---

## 📁 Project Architecture

```text
student.management.system/
│
├── main.py          # Application entry point & interactive console menu
├── student.py       # Core student operations & logic implementation
├── database.py      # JSON file handling mechanisms (load/save)
└── students.json    # Local database storage file
