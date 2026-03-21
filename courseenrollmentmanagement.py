def add_student(enrollments, course, roll):
    if course not in enrollments:
        enrollments[course] = set()
    enrollments[course].add(roll)
    print("Student added successfully")

def remove_student(enrollments, course, roll):
    if course in enrollments and roll in enrollments[course]:
        enrollments[course].remove(roll)
        print("Student removed successfully")
    else:
        print("Course not found or student not enrolled")

def display_course(enrollments, course):
    if course in enrollments:
        print("Students:", enrollments[course])
    else:
        print("Course not found")

def list_courses(enrollments):
    if enrollments:
        print("Courses:", list(enrollments.keys()))
    else:
        print("No courses available")

def check_student(enrollments, roll):
    courses = []
    for course in enrollments:
        if roll in enrollments[course]:
            courses.append(course)

    if courses:
        print("Student enrolled in:", courses)
    else:
        print("Student not enrolled in any course")

def enrollment_counts(enrollments):
    for course in enrollments:
        print(course, ":", len(enrollments[course]), "students")


# Main Menu Program
enrollments = {
    "Python": {101, 102, 105},
    "Data Science": {102, 103}
}

while True:
    print("\n1.Add Student")
    print("2.Remove Student")
    print("3.Display Course Students")
    print("4.List Courses")
    print("5.Check Student Enrollment")
    print("6.Show Enrollment Count")
    print("7.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        course = input("Enter course name: ")
        roll = int(input("Enter roll number: "))
        add_student(enrollments, course, roll)

    elif choice == 2:
        course = input("Enter course name: ")
        roll = int(input("Enter roll number: "))
        remove_student(enrollments, course, roll)

    elif choice == 3:
        course = input("Enter course name: ")
        display_course(enrollments, course)

    elif choice == 4:
        list_courses(enrollments)

    elif choice == 5:
        roll = int(input("Enter roll number: "))
        check_student(enrollments, roll)

    elif choice == 6:
        enrollment_counts(enrollments)

    elif choice == 7:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")