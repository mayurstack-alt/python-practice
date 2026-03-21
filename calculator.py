a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("Sum:",a+b)
if(a>b):
    print("Difference:",a-b)
else:
    print("Difference:",b-a)
print("Product:",a*b)
print("Integer Quotient:",a//b)
print("Floating Quotient:",round((a/b),2))
print("Remainder:",a%b)