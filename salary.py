#  salary breakdown
basicSalary=float(input("Enter the salary:"))
HRA=0.20*basicSalary
DA=0.10*basicSalary
Total=basicSalary+HRA+DA

print("SALARY EXPENSE")
print("HRA         :"+str(HRA))
print("DA          :"+str(DA))
print("Total Salary:"+str(Total))
