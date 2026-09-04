print("===== STUDENT DIRECTORY =====")

students = [
    {"name": "Prince", "age": 23, "course": "IT"},
    {"name": "Rahul", "age": 22, "course": "CSE"},
    {"name": "Amit", "age": 21, "course": "ECE"},
    {"name": "Neha", "age": 22, "course": "IT"},
    {"name": "Priya", "age": 21, "course": "CSE"}
]

search_name = input("Enter student name to search: ")

found = False

for student in students:
    if student["name"].lower() == search_name.lower():
        print("\nStudent Found!")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")
        found = True
        break

if not found:
    print("Student not found.")

