import json

def loadStudents():
    try:
        with open("students.json", "r") as f:
            return json.load(f)
    except:
        return []

def saveStudents(students):
    try:
        with open("students.json", "w") as f:
            json.dump(students, f, indent=4)
        return True
    except:
        return False