n=int(input("Enter year:"))
if((n%4==0 and n%100!=0) or (n%400==0)):
    print(n,"is a Leap year")
else:
    print(n,"is not a Leap year")
