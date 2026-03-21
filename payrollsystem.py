class Employee():
    def __init__(self,empId,name,basicSalary,rating):
        self.__empId=empId
        self.__name=name
        self.__basicSalary=basicSalary
        self.__rating=rating

    def set_salary(self,salary):
        if(salary>0):
            self.__basicSalary=salary
        else:
            print("Invalid Salary!")

    def rating(self,rating):
        if rating>=1 and rating<=5:
            self.__rating=rating
        else:
            print("Invalid Rating!")

    def calculate_net_salary(self):
        if self.__rating==5:
            bonus=0.02
        elif self.__rating==4:
            bonus=0.15
        elif self.__rating==3:
            bonus=0.1
        elif self.__rating==2:
            bonus=0.05
        else:
            bonus=0
        net_salary=self.__basicSalary+(self.__basicSalary*bonus)
        return net_salary
    
    def display(self):
        print("Employee ID:", self.__empId)
        print("Name:", self.__name)
        print("Basic Salary:", self.__basicSalary)
        print("Rating:", self.__rating)

while True:

    print("\n1. Add Employee")
    print("2. Calculate Net Salary")
    print("3. Display Employee Details")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        empId = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        salary = float(input("Enter Basic Salary: "))
        rating = int(input("Enter Rating (1-5): "))

        emp = Employee(empId, name, salary, rating)
        print("Employee Added Successfully")

    elif choice == 2:
        print("Net Salary:", emp.calculate_net_salary())

    elif choice == 3:
        emp.display()

    elif choice == 4:
        print("Program Terminated")
        break

    else:
        print("Invalid Choice")