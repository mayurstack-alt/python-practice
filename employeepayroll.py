class Employee:
    def __init__(self):
        self.__empId = None
        self.__name = None
        self.__basicSalary = 0
        self.__rating = 0

    def set_empId(self, empId):
        self.__empId = empId

    def set_name(self, name):
        self.__name = name

    def set_basicSalary(self, salary):
        if salary > 0:
            self.__basicSalary = salary
        else:
            print("Invalid Salary")

    def set_rating(self, rating):
        if 1 <= rating <= 5:
            self.__rating = rating
        else:
            print("Invalid Rating")

    def calculate_net_salary(self):
        if self.__rating == 5:
            bonus = 0.20
        elif self.__rating == 4:
            bonus = 0.15
        elif self.__rating == 3:
            bonus = 0.10
        elif self.__rating == 2:
            bonus = 0.05
        else:
            bonus = 0.0

        return self.__basicSalary + (self.__basicSalary * bonus)

    def display(self):
        print("\nEmployee Details:")
        print("ID:", self.__empId)
        print("Name:", self.__name)
        print("Basic Salary:", self.__basicSalary)
        print("Rating:", self.__rating)

emp = Employee()

while True:
    print("\n--- Employee Payroll System ---")
    print("1. Add Employee")
    print("2. Calculate Net Salary")
    print("3. Display Employee Details")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        empId = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        salary = float(input("Enter Basic Salary: "))
        rating = int(input("Enter Rating: "))

        emp.set_empId(empId)
        emp.set_name(name)
        emp.set_basicSalary(salary)
        emp.set_rating(rating)

        print("Employee Added Successfully")

    elif choice == 2:
        net_salary = emp.calculate_net_salary()
        print("Net Salary:", net_salary)

    elif choice == 3:
        emp.display()

    elif choice == 4:
        print("Program Terminated.")
        break

    else:
        print("Invalid Choice")