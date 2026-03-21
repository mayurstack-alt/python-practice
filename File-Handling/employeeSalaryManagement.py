def add_Employee():
    empId=str(input("Enter Employee ID:"))
    empName=str(input("Enter Employee Name:"))
    dept=str(input("Enter Department:"))
    salary=int(input("Enter Salary:"))
    with open("employee.txt","a") as file:
        file.write(empId+" "+empName+" "+dept+" "+str(salary)+"\n")
        
    print("Record added sucessfully")

def display_all_Employees():
    print("Employee Records")
    print("-"*20)
    with open("employee.txt","r") as file:
        content=file.read()
        if not content:
            print("No records Found")
        else:
            print(content)
        
def cal_total_salary():
    salary=0
    with open("employee.txt","r") as file:
        for line in file:
            data=line.strip().split()
            if(len(data)==4):
                salary+=int(data[3])
        
    print("Total Salary Expense=",salary)
        
while(1):
    print("1.Add Employee\n2.Display Employees\n3.Calculate Total Salary Expense\n4.Exit")
    choice=int(input("Enter choice:"))
    if(choice==1):
        add_Employee()
    elif(choice==2):
        display_all_Employees()
    elif(choice==3):
        cal_total_salary()
    elif(choice==4):
        print("Terminating program..")
        break
    else:
        print("Invalid Choice")





