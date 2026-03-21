def add_students():
    StudentId = input("Enter Student ID:")
    StudentName = input("Enter Student name:")
    CourseName = input("Enter Course name:")
    FeesPaid = int(input("Enter Fees Paid:"))

    with open("students.txt", "a") as f:
        f.write(StudentId + " " + StudentName + " " + CourseName + " " + str(FeesPaid) + "\n")


def view_students():
    print("Students Records")
    print("-" * 20)
    with open("students.txt", "r") as f:
        content=f.read()
        if not content:
            print("No records Found")
        else:
            print(content)


def search_student_by_id():
    searchStudentId = input("Enter Student ID to search:")
    found = False

    with open("students.txt", "r") as f:
        for line in f:
            data = line.split()
            if (len(data)==4 and data[0] == searchStudentId):
                print("Student Found")
                print(line)
                found = True
                break

    if not found:
        print("Student Not Found")


while True:
    print("1. Add Student Record\n2. View All Students\n3. Search Student By ID\n4. Exit")
    choice = int(input("Enter choice:"))

    if choice == 1:
        add_students()
        print("Student record added successfully")
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student_by_id()
    elif choice == 4:
        print("Terminating program..")
        break
    else:
        print("Invalid Choice")