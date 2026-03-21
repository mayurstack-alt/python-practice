# swap two numbers without using the third variable

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("Before Swap:")
print("a=",a)
print("b=",b)
a=a+b
b=a-b
a=a-b
print("After Swap:")
print("a=",a)
print("b=",b)